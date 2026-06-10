# Penjelasan Lengkap Source Code (Tubes DKA)

Dokumen ini membedah secara lengkap setiap bagian dari *source code* yang ada di dalam Jupyter Notebook untuk keperluan presentasi dan tanya jawab dosen.

---

## BAGIAN 1: PERSIAPAN DAN FUZZY INFERENCE SYSTEM (FIS)

### 1. Deklarasi Fungsi Keanggotaan (Membership Function)
Kita tidak menggunakan library bawaan (seperti `scikit-fuzzy`), melainkan mendefinisikan fungsinya dari awal (*from scratch*):
- `trapmf(x, a, b, c, d)`: Membentuk kurva berbentuk Trapesium. Nilai akan bernilai 1 jika $x$ berada di antara $b$ dan $c$. Jika di luar itu, nilainya akan menurun secara linear (miring) atau bernilai 0.
- `trimf(x, a, b, c)`: Membentuk kurva berbentuk Segitiga. Memiliki titik puncak tunggal pada $b$ (bernilai 1).

### 2. Definisi Himpunan Fuzzy Input
Kita membagi 3 parameter input ke dalam kategori-kategori menggunakan fungsi Trapesium yang sudah dibuat:
1. **Usia:** 
   - `Muda`: Dominan di usia 25-40 tahun.
   - `Sedang`: Dominan di usia 40-55 tahun.
   - `Tua`: Dominan di usia > 62 tahun.
2. **Tekanan Darah (ap_hi):** 
   - `Normal`: 70 - 110 mmHg.
   - `Pre-Hipertensi`: 125 - 135 mmHg.
   - `Hipertensi`: > 145 mmHg.
3. **BMI:** 
   - `Normal`: 15 - 22.
   - `Overweight`: 26 - 28.
   - `Obesitas`: > 32.

### 3. Definisi Output (Mamdani & Sugeno)
- **Mamdani:** Output direpresentasikan sebagai area/kurva fungsi keanggotaan (`Rendah`, `Sedang`, `Tinggi`).
- **Sugeno:** Output direpresentasikan sebagai sebuah konstanta angka tunggal (disebut *singleton*).
  - Rendah = 20.0
  - Sedang = 50.0
  - Tinggi = 85.0

### 4. Evaluasi Rule (Aturan Logika)
Di variabel `RULES`, kita mendefinisikan 27 kombinasi IF-THEN.
Fungsi `evaluasi_rule` bekerja dengan:
- Menghitung derajat kecocokan (`alpha`) untuk setiap kombinasi input.
- Menggunakan operator **AND** (yang di kode ditulis dengan fungsi `min()`). Artinya, jika rule berbunyi "Muda (0.8) DAN Hipertensi (0.2)", maka kekuatan (firing strength) dari rule tersebut diambil yang terkecil, yaitu `0.2`.

### 5. Inferensi Mamdani & Defuzzifikasi Centroid
Fungsi `mamdani_inferensi`:
1. **Implikasi (Clipping):** Memotong atap kurva output berdasarkan nilai `alpha` dari rule yang aktif.
2. **Agregasi:** Menggabungkan semua kurva output yang terpotong menjadi satu luasan baru menggunakan fungsi maksimum (`np.maximum`).
3. **Defuzzifikasi:** Mencari "titik berat" (Centroid) dari luasan agregasi tersebut menggunakan rumus integral matematika yang diwujudkan dengan deret numerik `np.sum(S_vals * y_agg) / denom`.

### 6. Inferensi Sugeno & Weighted Average
Fungsi `sugeno_inferensi`:
- Cara kerja jauh lebih sederhana. Sistem mengalikan `alpha` tiap rule yang aktif dengan nilai konstanta outputnya (*singleton*).
- Lalu mencari rata-ratanya menggunakan rumus matematika **Weighted Average** (Nilai Total / Total Bobot Alpha).
- Inilah alasan kenapa Sugeno komputasinya jauh lebih ringan dan cepat dibandingkan perhitungan integral Mamdani.

---

## BAGIAN 2: EVALUASI MENGGUNAKAN DEEP LEARNING

Deep Learning digunakan untuk memvalidasi dan membandingkan ketepatan (akurasi) Fuzzy terhadap data pasien yang sebenarnya (*ground truth*).

### 1. Load Data & Preprocessing (Scikit-Learn & Pandas)
- `pd.read_excel(EXCEL_PATH)`: Memuat 70.000 data ke dalam *Dataframe*.
- **Membersihkan Data:** Fitur tekanan darah tinggi dibatasi (`clip`) di rentang wajar (60-250) agar model tidak hancur karena data tidak masuk akal (misal tekanan darah -100).
- `train_test_split(X, y, test_size=0.2)`: Memotong data menjadi 80% untuk dipelajari mesin (Train), dan 20% untuk ujian mandiri mesin (Test).
- `StandardScaler`: *Neural network* sangat sensitif terhadap nilai angka yang jauh berbeda (misal usia 50 vs BMI 20). Scaler akan menyamakan rata-rata (*mean*) dan sebaran (*std*) seluruh fitur agar proses belajar cepat dan stabil.

### 2. Arsitektur Model Deep Learning (Keras/TensorFlow)
Kita menggunakan fungsi `Sequential()` untuk menumpuk lapisan "otak buatan" (*Multi-Layer Perceptron*):
- `Dense(32, activation='relu')`: Lapis pertama, memiliki 32 neuron yang saling terkoneksi. `ReLU` digunakan agar mesin bisa belajar membedakan pola batas yang tidak lurus (non-linear).
- `Dropout(0.2)`: Mengunci/mematikan 20% neuron secara acak di setiap putaran belajar. Ini memaksa model untuk mencari pola general, bukan sekadar "menghafal" jawaban soal latih.
- `Dense(1, activation='sigmoid')`: Lapis terakhir (Output). Aktivasi `sigmoid` mengonversi perhitungan bebas ke angka final berbentuk probabilitas biner: **0.0 (Sehat) hingga 1.0 (Penyakit Kardiovaskular)**.

### 3. Kompilasi & Training
- `loss='binary_crossentropy'`: Fungsi hukuman yang bertugas mengukur seberapa meleset tebakan mesin dari kunci jawaban (*cardio*). Model akan berusaha menekan nilai loss ini serendah mungkin.
- `optimizer='adam'`: Algoritma cerdas untuk meng-update "bobot/parameter" otak di setiap putaran belajar (*epoch*) secara sangat efisien.
- `model.fit(..., epochs=30)`: Proses mesin menelan data 80% dan membandingkannya dengan 20% soal ujian sebanyak 30 putaran.

### 4. Plot Evaluasi
- **Grafik Loss & Accuracy**: Menunjukkan performa model. Jika garis *Train* dan *Val* berhimpitan dan naik secara stabil, artinya model belajar dengan sangat sehat (tidak Underfit / Overfit).
- **Confusion Matrix**: Peta visual (kotak warna biru) untuk melihat secara detail berapa orang sehat yang ditebak sakit (False Positive), dan sebaliknya. Ini lebih jujur dibandingkan sekadar persentase Akurasi.

---

## BAGIAN 3: PENJELASAN GRAFIK (VISUALISASI) YANG DIGUNAKAN
Di dalam notebook, kita menggunakan berbagai jenis visualisasi (grafik) menggunakan library `matplotlib` dan `seaborn` untuk membuat analisis data menjadi lebih informatif secara visual. Jika ditanya oleh dosen, berikut adalah penjelasan setiap grafik tersebut:

### 1. Grafik pada Model Fuzzy (Mamdani & Sugeno)
* **Grafik Agregasi & Defuzzifikasi Mamdani (Fill-Between Plot):**
  - **Fungsi:** Menampilkan bagaimana kurva output (`Rendah`, `Sedang`, `Tinggi`) terpotong (clipping) berdasarkan nilai bobot $\alpha$ (*firing strength*). 
  - **Bentuk Visual:** Berupa area berwarna biru, hijau, dan oranye yang digabung (*aggregated area*). Terdapat sebuah garis putus-putus lurus ke bawah yang menunjukkan titik pusat massa (*Centroid*). Nilai di garis inilah yang menjadi **hasil persentase tebakan akhir** untuk pasien.
* **Dashboard Visual Sugeno (Grid Plot dengan 4 Panel):**
  - **Panel 1 & 2 (Line Plot & Vertical Line):** Menampilkan fungsi keanggotaan input (Usia dan Tekanan Darah). Garis putus-putus merah menunjukkan letak nilai pasti pasien di dalam kurva tersebut.
  - **Panel 3 (Bar Chart Horizontal):** Menampilkan *firing strength* (seberapa kuat rule yang "aktif" menyala). Semakin panjang baloknya, semakin besar rule tersebut mengambil keputusan.
  - **Panel 4 (Bar Chart Vertikal):** Menampilkan kontribusi nyata dari masing-masing rule yang aktif (bobot $\alpha$ dikali nilai konstan $z$). Garis putus-putus horizontal berwarna merah adalah **hasil akhir** (*Weighted Average*).
* **Grafik Perbandingan Pasien (Subplots):**
  - Digunakan di bagian akhir eksperimen Fuzzy untuk membandingkan secara visual dashboard Sugeno dari dua/lebih pasien yang berbeda (misalnya Pasien A vs Pasien B) dalam satu layar, sehingga kita tahu mengapa Pasien A "Berisiko" dan Pasien B "Aman".

### 2. Grafik pada Model Deep Learning
* **Grafik Learning Curves (Line Plot - Matplotlib):**
  - **Fungsi:** Merekam jejak langkah proses "belajar" mesin di tiap iterasi (*epoch*). Terdiri dari 2 grafik: *Loss Curve* (tingkat kesalahan) dan *Accuracy Curve* (tingkat kebenaran).
  - **Cara Menjelaskan ke Dosen:** Terdapat dua garis di tiap grafik. Garis *Train* (hasil saat belajar) dan garis *Validation* (hasil ujian akhir). Model yang cerdas dan tangguh ditandai dengan garis *Loss* yang menurun mulus mendekati nol, dan *Accuracy* yang naik mulus ke atas, di mana kedua garis tersebut tidak terlalu berjarak lebar. Jika berjarak sangat jauh, modelnya dicap **Overfitting** (tukang hafal tapi tidak paham konsep).
* **Confusion Matrix (Heatmap - Seaborn):**
  - **Fungsi:** Tabel kotak matriks berwarna biru yang menunjukkan distribusi akurasi tebakan model dengan sangat merinci.
  - **Cara Menjelaskan ke Dosen:** 
    - **Kiri Atas (True Negative):** Jumlah orang yang benar-benar SEHAT dan sukses ditebak SEHAT.
    - **Kanan Bawah (True Positive):** Jumlah orang yang SAKIT kardiovaskular dan sukses ditebak SAKIT.
    - **Kanan Atas (False Positive):** Orang sehat, tapi panik karena ditebak sakit.
    - **Kiri Bawah (False Negative):** Orang sakit parah, tapi dibilang sehat. (Dalam bidang medis, matriks ini sangat penting karena kita harus menekan angka di kotak Kiri Bawah menjadi sekecil mungkin agar tidak salah diagnosa pasien!).

---

### *Key Takeaways* untuk Presentasi Dosen
Jika dosen bertanya, **"Kenapa pakai keduanya?"**
**Jawab:**
"Fuzzy Inference System memberikan *transparansi*, logikanya dapat dibaca dan divalidasi langsung oleh dokter (White-Box). Namun penentuan batas usianya kaku. Oleh karena itu, Deep Learning digunakan sebagai perbandingan yang berbasis 100% pada *Machine Learning (Black-Box)* untuk menemukan pola probabilitas statistik langsung dari 70.000 sejarah rekam medis pasien di dunia nyata."

---

## # Revisi 1: Penambahan Evaluasi Performa & Integrasi Deep Learning (Hybrid Neuro-Fuzzy)

Pada revisi ini, **kode Fuzzy Logic yang sudah ada (Section 1-12) TIDAK diubah sama sekali**. Yang dilakukan adalah **menambahkan 3 section baru di akhir notebook** untuk memenuhi kebutuhan evaluasi dan mendapatkan **Bonus 20 Poin** (Deep Learning).

### 1. Section 13 — Evaluasi Performa Fuzzy (Baru)
- **Tujuan:** Mengukur dan membandingkan performa Mamdani vs Sugeno secara kuantitatif.
- **Cara Kerja:** Menggunakan data hasil batch inferensi dari Section 10-11 (`df_raw` yang sudah memiliki kolom `mamdani_score` dan `sugeno_score`).
- **Metrik:** Menghitung *Accuracy*, *Precision*, *Recall*, dan *F1-Score* untuk kedua metode.
- **Threshold:** Skor Fuzzy ≥ 55% dianggap prediksi **Sakit (1)**, di bawah 55% dianggap **Tidak Sakit (0)**.

### 2. Section 14 — Integrasi Deep Learning Keras Hybrid (Baru)
- **Aturan yang dipenuhi:** Bonus 20 poin (Fuzzy + Deep Learning) di mana DL tidak menggantikan Fuzzy, melainkan berjalan bersama.
- **Arsitektur:** Multi-Layer Perceptron (Keras Sequential) dengan layer Dense(64) → Dropout(0.3) → Dense(32) → Dropout(0.2) → Dense(16) → Dense(1, sigmoid).
- **Pendekatan Hybrid:** Fitur asli (`age`, `ap_hi_clean`, `bmi_clean`) **digabungkan** dengan skor output dari perhitungan Fuzzy (`mamdani_score`). Output Fuzzy ini bertindak sebagai *expert feature* (skor pakar) tambahan. Deep Learning kemudian mempelajari bobot semua fitur ini untuk menghasilkan akurasi yang lebih tinggi.
- **Bukti:** Deep Learning disokong oleh logika Fuzzy dan bekerja secara komplementer, bukan menggantikan.

### 3. Section 15 — Kesimpulan Akhir (Baru)
- Menyimpulkan perbandingan Mamdani vs Sugeno.
- Menyimpulkan bahwa pendekatan Hybrid (Fuzzy + Deep Learning) adalah yang terbaik karena menggabungkan transparansi logika Fuzzy (White-Box) dengan kemampuan belajar Deep Learning (Black-Box).
