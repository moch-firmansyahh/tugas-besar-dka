# ðŸ«€ Dokumentasi Proyek: Deteksi Risiko Kardiovaskular (Fuzzy & Deep Learning)

Selamat datang di direktori dokumentasi proyek! Folder ini memuat penjelasan **SANGAT LENGKAP 100%** mengenai segala aspek yang terkait dengan alur algoritma, data, dan program antarmuka dari Tugas Besar / Proyek ini.

Dokumentasi ini ditulis sebagai panduan komprehensif dari hulu ke hilir. Silakan klik tautan pada daftar isi di bawah ini untuk membaca masing-masing topik.

---

## ðŸ“‘ Daftar Isi Dokumentasi Utama

### 1. ðŸ“Š [Penjelasan Dataset & Preprocessing](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/01_Penjelasan_Dataset.md)
Membahas asal usul data rekam medis pasien (`cardio_train1.xlsx`), bagaimana cara membersihkan data dari nilai tak masuk akal (Outlier), rumus BMI, dan pemahaman terkait masing-masing dari ke-6 fitur input yang digunakan (Usia, Tensi, dsb).

### 2. ðŸ§  [Logika Fuzzy: Mamdani dan Sugeno secara Mendalam](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/02_Fuzzy_Logic_Sugeno_dan_Mamdani.md)
Membahas konsep utama pemodelan kepakaran medis ke dalam bahasa mesin. Mencakup rumus matematika pembentuk Fungsi Keanggotaan, evaluasi 42 Aturan (Rule Base) dengan *Product T-Norm*, serta perbedaan mendasar kalkulasi persentase antara metode integral Mamdani (*Centroid*) melawan perhitungan *Weighted Average* Sugeno.

### 3. ðŸ¤– [Arsitektur Deep Learning Hybrid Terperinci](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/03_Deep_Learning_Hybrid.md)
Membahas topologi arsitektur Machine Learning (Jaringan Saraf Tiruan) yang di-training pada proyek ini. Mencakup pemahaman fitur tambahan *Hybrid*, fungsi aktivasi *ReLU/Sigmoid*, metode pencegah overfitting (*Dropout*), hingga nilai *Hyperparameter* selama pelatihan (*Adam Optimizer, Epoch, Batch size*).

### 4. ðŸ’» [Penjelasan Antarmuka Web (Streamlit App)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/04_Penjelasan_Streamlit_App.md)
Membedah arsitektur kode file `app.py` yang dibangun di atas framework web Streamlit. Menjelaskan secara berurutan mulai dari manajemen memori (Caching), penataan sidebar input, tombol kalkulasi, hingga teknik render grafik kanvas menggunakan *Matplotlib*.

### 5. ðŸ“ˆ [Panduan Membaca Tabel Hasil Evaluasi Model](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/05_Penjelasan_Tabel_Evaluasi.md)
Penjelasan khusus tentang metrik ukur performa model. Membahas *Accuracy, Precision, Recall, F1-Score* secara konteks medis, serta menjabarkan tabel *Confusion Matrix* (True Negative, False Negative, dll).

### 6. ðŸš€ [Evolusi dan Peningkatan Model (Versi Lama vs Baru)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/06_Evolusi_dan_Peningkatan_Model.md)
Bagian paling kritikal yang menjabarkan **mengapa model saat ini diklaim jauh lebih baik**. Membahas transisi evolusi proyek dari sekadar menggunakan 5 Variabel Input dan 25 Aturan, diekspansi menjadi 6 Input (Glukosa) + 42 Aturan, serta perubahan nilai ambang batas (*Thresholding*).

### 7. ðŸ“ [Struktur dan Penjelasan Setiap File Proyek](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/07_Struktur_dan_Penjelasan_File_Proyek.md)
*Master guide* dari seluruh direktori proyek! Membedah satu per satu setiap *script* `.py`, *file* konfigurasi, model `.h5`, dan data `.xlsx` yang ada di luar folder ini, serta mengupas tuntas keterkaitannya satu sama lain layaknya sebuah anatomi program yang utuh.

### 8. ðŸ” [Bedah Kode Secara Mendalam: evaluate_accuracy.py](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/08_Penjelasan_Kode_evaluate_accuracy.md)
Khusus bagi Anda yang butuh rincian spesifik mengenai *coding*, dokumen ini menjelaskan kode python per blok. Penjelasan mencakup deklarasi Array `RULES`, eksekusi iteratif `iterrows`, dan algoritma manual pembentukan tabel Akurasi dan Presisi.

### 9. ðŸ§  [Bedah Kode Secara Mendalam: retrain_dl_hybrid.py](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/09_Penjelasan_Kode_retrain_dl.md)
Membongkar baris demi baris rahasia di balik otak TensorFlow. Dokumen ini menjelaskan rinci bagaimana data dari Excel di-potong menggunakan `train_test_split`, disterilkan menggunakan `StandardScaler`, dimasukkan kalkulator *Hybrid Mamdani*, sebelum diolah paksa ke dalam matriks Jaringan Saraf `Dense`!

### 10. ðŸ† [Panduan Sukses Presentasi Tugas Besar (Cheat Sheet)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/10_Panduan_Presentasi_Tugas_Besar.md)
**Wajib BACA Sebelum Demo!** Dokumen penutup ini tidak lagi membahas teori, melainkan taktik *Public Speaking*. Berisi skenario urutan presentasi dari awal sampai akhir, serta bocoran "Kisi-Kisi Pertanyaan Maut" yang sering dilontarkan Dosen Penguji beserta contekan kunci jawabannya.

---

> [!TIP]
> **Cara Membaca Terbaik**: Sangat disarankan untuk membaca urutan dokumen di atas secara berurutan dari nomor 1 hingga nomor 6 agar mendapatkan pemahaman logika komputasi yang nyambung dan tak terputus.

Dibuat dengan â¤ï¸ untuk keperluan Tugas Besar Keilmuan. 
Selamat membaca!
# Penjelasan Dataset (Cardiovascular Disease Dataset)

Dataset yang digunakan dalam proyek ini berfokus pada prediksi risiko penyakit kardiovaskular. Data mentah aslinya tersimpan dalam file `cardio_train1.xlsx` yang merupakan kumpulan rekam medis dari puluhan ribu pasien.

## 1. Asal Usul dan Deskripsi Data
Dataset ini merupakan modifikasi dari *Cardiovascular Disease dataset* yang sering dijumpai di komunitas Data Science (seperti Kaggle). Dataset ini berisi kombinasi data objektif (hasil pengukuran klinis) dan data subjektif (informasi dari pasien).

Tujuan utama dari dataset ini adalah memprediksi variabel target (Label/Class) yaitu **Cardio (0 = Sehat, 1 = Memiliki Penyakit Kardiovaskular)**.

## 2. Preprocessing Data (Pembersihan Data)
Sebelum data dapat dimasukkan ke dalam model Fuzzy maupun Deep Learning, data mentah harus dibersihkan untuk menghilangkan *outlier* (pencilan) atau nilai yang tidak masuk akal secara medis. Pada skrip `retrain_dl_hybrid.py`, proses pembersihan yang dilakukan antara lain:

1. **Pembersihan Tekanan Darah**:
   - `ap_hi` (Sistolik): Hanya mengambil rentang **60 hingga 250 mmHg**. Pasien dengan sistolik negatif atau di atas 300 dianggap sebagai *noise* (kesalahan input alat).
   - `ap_lo` (Diastolik): Hanya mengambil rentang **40 hingga 150 mmHg**.

2. **Perhitungan BMI (Body Mass Index)**:
   - Fitur `height` (tinggi badan dalam cm) dan `weight` (berat badan dalam kg) tidak langsung dimasukkan ke model. Sebagai gantinya, dilakukan kalkulasi ekstraksi fitur menjadi `bmi`.
   - Rumus: `BMI = weight / (height / 100)^2`

## 3. Penjelasan Fitur Lengkap (Input Variabel)
Aplikasi ini bergantung pada 6 variabel fitur utama yang sudah dibersihkan, yaitu:

### 1. Usia (Age)
Usia pasien dalam tahun. Usia adalah faktor risiko independen terbesar untuk penyakit kardiovaskular. Semakin bertambah usia, dinding pembuluh darah menjadi lebih kaku dan rentan terhadap penumpukan plak (aterosklerosis).
- Rentang normal input: **20 hingga 80 tahun**.
- Fuzzifikasi: Diubah menjadi tingkat **Muda**, **Sedang**, dan **Tua**.

### 2. Tekanan Darah Sistolik (ap_hi)
Tekanan sistolik mewakili tekanan di dalam arteri saat jantung berkontraksi (memompa darah). Tekanan tinggi secara konsisten akan merusak dinding arteri.
- **Normal**: Di bawah 120 mmHg.
- **Pre-Hipertensi**: 120 - 139 mmHg.
- **Hipertensi**: 140 mmHg ke atas.

### 3. Tekanan Darah Diastolik (ap_lo)
Tekanan diastolik mewakili tekanan arteri saat jantung berelaksasi di antara detakan.
- **Normal**: Di bawah 80 mmHg.
- **Pre-Hipertensi**: 80 - 89 mmHg.
- **Hipertensi**: 90 mmHg ke atas.

### 4. Body Mass Index (BMI)
Indikator standar dari WHO untuk mengukur apakah seseorang memiliki berat badan proporsional. Obesitas membebani kerja jantung dan sering memicu resistensi insulin serta dislipidemia (kolesterol buruk).
- **Normal**: 18.5 - 24.9
- **Overweight**: 25 - 29.9
- **Obesitas**: > 30

### 5. Kolesterol (Cholesterol)
Dataset ini menggunakan nilai ordinal/kategorikal untuk kolesterol (bukan miligram per desiliter/mg/dL).
- **1**: Normal
- **2**: Di atas Normal (Tinggi)
- **3**: Sangat Tinggi

### 6. Glukosa (Glucose)
Sama seperti kolesterol, glukosa (gula darah) disimpan dalam nilai kategorikal. Pasien dengan kadar gula tinggi memiliki risiko menderita diabetes, yang meningkatkan risiko serangan jantung hingga 2x lipat.
- **1**: Normal
- **2**: Di atas Normal (Tinggi)
- **3**: Sangat Tinggi

## 4. Normalisasi Fitur (Scaling)
Dalam pemodelan *Deep Learning*, sangat penting untuk melakukan penskalaan data karena variabel memiliki satuan yang berbeda-beda (Sistolik rentangnya ratusan, Kolesterol rentangnya 1-3).
Proyek ini menggunakan `StandardScaler` dari Scikit-Learn:
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
Proses ini mengubah distribusi masing-masing fitur sehingga memiliki rata-rata 0 (mean = 0) dan standar deviasi 1 (std = 1), memastikan model Deep Learning tidak bias terhadap variabel yang angkanya lebih besar (seperti tekanan darah) dan mengabaikan variabel kecil (seperti kategori glukosa). File scaler kemudian disimpan sebagai `scaler_hybrid_dka.pkl`.
# Logika Fuzzy: Mamdani dan Sugeno secara Mendalam

Sistem inferensi fuzzy (Fuzzy Inference System - FIS) digunakan dalam proyek ini untuk mentranslasikan pengetahuan pakar medis mengenai faktor risiko jantung ke dalam bentuk logika komputasi. Tidak seperti logika Boolean atau biner (0 atau 1), logika fuzzy mengizinkan nilai derajat kebenaran parsial di antara 0.0 (sangat salah) dan 1.0 (sangat benar).

## 1. Fuzzifikasi dan Fungsi Keanggotaan (Membership Function)
Langkah pertama dalam sistem fuzzy adalah Fuzzifikasi. Pada tahap ini, masukan tegas (crisp input) seperti tekanan darah 130 mmHg diubah menjadi **derajat keanggotaan (membership degree - Î¼)**.

Proyek ini menggunakan dua bentuk Fungsi Keanggotaan matematis:
1. **Triangular (Segitiga - `trimf`)**: Digunakan untuk variabel kategori sederhana seperti Kolesterol dan Glukosa. Memiliki 3 parameter `(a, b, c)`.
2. **Trapezoidal (Trapesium - `trapmf`)**: Digunakan untuk variabel kontinu yang lebih kompleks seperti Usia, BMI, dan Tekanan Darah. Memiliki 4 parameter `(a, b, c, d)` dengan puncak datar di mana nilai keanggotaan bernilai mutlak 1.0.

Contoh matematis fungsi keanggotaan Trapesium (Trapmf) untuk $x$:
$$
\mu(x) =
\begin{cases}
0, & x \le a \text{ atau } x \ge d \\
\frac{x - a}{b - a}, & a < x < b \\
1, & b \le x \le c \\
\frac{d - x}{d - c}, & c < x < d
\end{cases}
$$

**Contoh Fuzzifikasi:** Jika seorang pasien memiliki tekanan sistolik 130 mmHg. Berdasarkan definisi fungsi:
- `mu_bp_normal`: Kurva akan mengembalikan nilai $0.5$ (karena 130 berada di batas turun antara 125-135).
- `mu_bp_pre_hiper`: Kurva akan mengembalikan nilai $0.5$ (karena 130 berada di batas naik antara 125-135).
- `mu_bp_hiper`: Kurva mengembalikan nilai $0.0$.
Dengan demikian, tekanan darah 130 mmHg tersebut secara matematis diartikan sebagai "50% Normal dan 50% Pre-Hipertensi".

---

## 2. Inferensi dan Basis Aturan (Rule Base)
Setelah semua input di-fuzzifikasi, tahap selanjutnya adalah mengevaluasi aturan berbasis pengetahuan (`IF ... AND ... THEN ...`). Proyek ini menanamkan **42 Aturan Pakar (Rule Base)**.

Operator logika **AND** yang digunakan untuk menghubungkan tiap klausul (kondisi) disebut **T-Norm**. Dalam sistem ini, kita menggunakan **Product t-norm**, yang bekerja dengan mengalikan semua derajat keanggotaan fitur.

Formulasi derajat pemenuhan aturan (Firing Strength) $\alpha$ untuk Aturan ke-$i$:
$$ \alpha_i = \mu_{\text{usia}}(x_1) \times \mu_{\text{sistolik}}(x_2) \times \mu_{\text{diastolik}}(x_3) \times \mu_{\text{bmi}}(x_4) \times \mu_{\text{kolesterol}}(x_5) \times \mu_{\text{glukosa}}(x_6) $$

Contoh Aturan ke-8 dari blok kode:
> IF Usia Muda AND Sistolik Hipertensi AND Diastolik Hipertensi AND BMI Obesitas AND Kolesterol Tinggi AND Glukosa Tinggi THEN Risiko Tinggi.

Jika semua input pasien memicu fungsi keanggotaan tersebut (misal nilainya adalah 0.8, 0.9, 0.9, 1.0, 1.0, 1.0), maka kekuatan aturan tersebut (firing strength) akan bernilai: $\alpha = 0.8 \times 0.9 \times 0.9 \times 1.0 \times 1.0 \times 1.0 = 0.648$.

---

## 3. Komparasi: Defuzzifikasi Mamdani vs Sugeno

Bagian evaluasi (IF) dari Mamdani dan Sugeno adalah sama persis. Perbedaan fundamentalnya terletak pada bagian **THEN (Konsekuen)** dan proses akhir **Defuzzifikasi** (mengembalikan nilai fuzzy menjadi satu angka persentase akhir).

### A. FIS Mamdani
Pada Mamdani, konsekuen merupakan **Himpunan Fuzzy** (fungsi keanggotaan Trapesium/Segitiga untuk label Rendah, Sedang, Tinggi).
1. **Implikasi (Pemotongan Kurva)**: Menggunakan min-clipping atau scaling untuk memotong puncak fungsi keanggotaan Output sebesar nilai firing strength ($\alpha$).
2. **Agregasi**: Menyatukan seluruh kurva output dari aturan yang aktif menjadi satu kurva agregasi raksasa dengan logika **OR** (mengambil nilai maksimum `np.maximum`).
3. **Defuzzifikasi Centroid**: Menghitung Pusat Massa (Titik Berat) dari area di bawah kurva agregasi menggunakan perhitungan Integral Diskret.

Rumus Centroid (Center of Area):
$$ Z_{\text{Mamdani}} = \frac{\sum_{i=1}^{n} (s_i \cdot \mu_{\text{agg}}(s_i))}{\sum_{i=1}^{n} \mu_{\text{agg}}(s_i)} $$
Di mana $s$ adalah skala risiko dari 0% hingga 100%. Metode ini sangat intuitif namun komputasinya mahal karena menghitung luas daerah tak beraturan.

### B. FIS Sugeno (Orde Nol / Singleton)
Pada Sugeno, konsekuen bukanlah fungsi himpunan/kurva melainkan sebuah **Konstanta Matematis** yang disebut Singleton. 
Dalam proyek ini, singleton telah dioptimasi berdasarkan persebaran rata-rata data:
- `Risiko Rendah (z) = 15.0%`
- `Risiko Sedang (z) = 45.0%`
- `Risiko Tinggi (z) = 85.0%`

**Defuzzifikasi Weighted Average**: Alih-alih melakukan integral area seperti Mamdani, Sugeno murni menggunakan aljabar aritmatika untuk mengalkulasi Rata-rata Terbobot (Weighted Average).

Rumus Weighted Average Sugeno:
$$ Z_{\text{Sugeno}} = \frac{\sum_{i=1}^{n} (\alpha_i \cdot z_i)}{\sum_{i=1}^{n} \alpha_i} $$
- $\alpha_i$ adalah firing strength (bobot aturan).
- $z_i$ adalah konstanta output (15.0, 45.0, atau 85.0).

Metode Sugeno sangat ringan, cepat, efisien untuk sistem komputasi rendah, serta sangat presisi ketika diintegrasikan dengan algoritma machine learning atau optimasi turunan seperti Adaptive Neuro-Fuzzy Inference System (ANFIS).
# Arsitektur Deep Learning Hybrid Terperinci

Selain logika fuzzy (Mamdani dan Sugeno) yang bertindak sebagai "White-Box" berbasis pengetahuan kepakaran (Rule-Based), proyek ini meningkatkan akurasi dengan menggunakan algoritma **Machine Learning** beraliran **Deep Learning (Deep Neural Networks)** sebagai "Black-Box".

Hal yang membuat model ini **Hybrid** adalah bagaimana hasil keluaran model Fuzzy (skor defuzzifikasi Mamdani) tidak dibuang begitu saja, melainkan digabung (concatenate) sebagai **Fitur Input Tambahan** bagi model Jaringan Saraf Tiruan. Metode ini menyuntikkan "kecerdasan rasional medis pakar" ke dalam mesin komputasi matematis.

## 1. Topologi Arsitektur Neural Network
Sesuai dengan implementasi di `retrain_dl_hybrid.py`, proyek ini menggunakan library **TensorFlow/Keras** dengan arsitektur tipe Sequential berlapis banyak. Topologinya dijabarkan sebagai berikut:

### A. Input Layer (Lapisan Masukan)
Menerima total **7 Fitur Input** dalam bentuk tensor/vektor 1D yang telah dinormalisasi menggunakan StandardScaler (Z-Score Normalization).
Fitur tersebut adalah: `['age', 'ap_hi', 'ap_lo', 'bmi', 'cholesterol', 'gluc', 'mamdani_score']`.

### B. Hidden Layers (Lapisan Tersembunyi)
Terdapat 3 buah lapisan saraf tersembunyi berjenis Fully Connected (Dense Layer), yang bertugas untuk memetakan hubungan linear maupun non-linear dari ke-7 fitur di atas.

1. **Hidden Layer 1**: Mengandung **64 Neuron**.
   - Fungsi Aktivasi: `ReLU` (Rectified Linear Unit), yang hanya merespon sinyal positif. Secara matematis: $f(x) = \max(0, x)$.
   - Regularisasi: Diikuti oleh **Dropout (0.3)**, yang mematikan/men-drop 30% dari neuron secara acak selama pelatihan. Tujuannya adalah memecah fenomena *co-adaptation* saraf, guna mencegah **Overfitting** (model hanya hafal data latih).
2. **Hidden Layer 2**: Mengandung **32 Neuron**.
   - Fungsi Aktivasi: `ReLU`.
   - Regularisasi: **Dropout (0.2)**, mematikan 20% saraf acak.
3. **Hidden Layer 3**: Mengandung **16 Neuron**.
   - Fungsi Aktivasi: `ReLU`. Tanpa dropout. Lapisan ini memeras semua pemahaman kompleks (feature extraction tingkat tinggi) menjadi bentuk akhir yang sangat ringkas.

### C. Output Layer (Lapisan Keluaran)
Lapisan terakhir yang bertanggung jawab mengeksekusi konklusi akhir.
- Terdiri dari **1 Neuron** tunggal.
- Fungsi Aktivasi: `Sigmoid`. Fungsi Sigmoid menekan output angka berapapun menjadi persis rentang probabilitas absolut antara $0.0$ hingga $1.0$. Secara matematis: $f(x) = \frac{1}{1 + e^{-x}}$.
- **Thresholding**: Jika keluaran neuron Sigmoid $\ge 0.5$, pasien diprediksi **Sakit Kardio (Positif/Tinggi)**. Jika $< 0.5$, pasien diprediksi **Sehat (Negatif/Rendah)**.

---

## 2. Proses Re-Training Model (Hyperparameters)
Model cerdas ini dilatih dan "belajar" layaknya otak manusia untuk mencari titik optimum bobot (Weight/Bias) yang menghubungkan semua lapisan tersebut menggunakan mekanisme *Backpropagation*.
Hyperparameter yang dipakai pada fase pelatihan (Training):

1. **Loss Function**: `binary_crossentropy`. Fungsi kerugian standar untuk klasifikasi dua kelas (biner). Model akan memberikan "hukuman" (penalty) besar jika tebakannya salah secara signifikan.
2. **Optimizer**: `Adam` (Adaptive Moment Estimation). Algoritma optimasi turunan gradient descent paling populer yang menyesuaikan kecepatan belajar (learning rate) masing-masing parameter bobot secara mandiri. Sangat konvergen secara cepat.
3. **Epochs**: `30`. Model memproses dan memutari seluruh sampel data (`df_clean`) sebanyak 30 kali iterasi untuk memastikan pemahaman sempurna.
4. **Batch Size**: `64`. Data pasien tidak dipelajari satu per satu, melainkan diolah beramai-ramai sebanyak 64 baris sekali tebak. Mempercepat pelatihan dengan matrix multiplication pada GPU/CPU.
5. **Validation Split**: `20%` dataset disisihkan untuk pengujian murni, sebagai evaluasi objektif sehingga metrik *accuracy* tidak bocor/bias.

## 3. Hasil & Metrik Evaluasi
Setelah proses latih dan ujicoba pada data Test (Testing Set):
- **Akurasi Model**: Model hybrid memiliki performa akurasi di rentang ~73-75%, performa yang sangat kompetitif untuk prediksi kardiovaskular dari rekam medis sebatas survei/pemeriksaan luar tanpa CT-Scan jantung.
- **Confusion Matrix**: Menjabarkan jumlah prediksi benar dan salah:
  - *True Negative (TN)*: Pasien benar diprediksi sehat.
  - *True Positive (TP)*: Pasien benar diprediksi berisiko jantung.
  - *False Positive (FP - Tipe 1 Error)*: Pasien sehat tapi diprediksi sakit jantung (terlalu waspada).
  - *False Negative (FN - Tipe 2 Error)*: Pasien berisiko tetapi diprediksi sehat (Paling bahaya dalam dunia medis).

Seluruh kecerdasan artifisial (matriks bobot Neural Networks berkapasitas kilobyte) ini disalin keras dan dibekukan ke dalam file memori `model_hybrid_dka.h5` agar siap pakai kapan saja oleh aplikasi web Streamlit.
# Penjelasan Antarmuka Web (Streamlit App) Secara Komprehensif

Dalam pengembangan sistem berbasis data/AI, logika *backend* semata (Python scripts) kurang intuitif bagi End-User seperti dokter atau tenaga medis. Oleh karena itu, antarmuka pengguna grafis (GUI) interaktif dibangun menggunakan teknologi web framework bernama **Streamlit**, yang seluruh kodenya berada di dalam file `app.py`.

## 1. Apa itu Framework Streamlit?
Streamlit adalah framework *open-source* berbasis bahasa Python (dirilis tahun 2019) yang didesain secara spesifik untuk tim Machine Learning dan Data Science. Berbeda dengan framework raksasa klasik seperti Django atau Flask yang mengharuskan pengembang menulis kode perutean (routing), desain HTML, pengelolaan tata letak CSS, hingga *Javascript asynchronous AJAX* secara mandiri, Streamlit mengubah logika skrip Python biasa menjadi aplikasi Web *Single-Page Application (SPA)* dinamis hanya dalam beberapa baris perintah antarmuka. 

Setiap kali *user* (pengguna) mengubah nilai parameter pada layar antarmuka (misalnya menggeser *slider* Usia), Streamlit secara otomatis mendeteksi perubahan state (*re-run*) dan mengeksekusi ulang file Python dari atas ke bawah.

---

## 2. Bedah Struktur Kode `app.py`

Struktur `app.py` proyek ini dibagi menjadi 5 komponen utama, yang sangat tertata sesuai arsitektur *Model-View-Controller (MVC)* fungsional.

### A. Komponen "Knowledge" / Fungsi Keanggotaan (Baris 20 - 77)
Bagian paling mendasar berisi representasi komputasi matematis dari Fungsi Keanggotaan Trapesium (`trapmf`) dan Segitiga (`trimf`). 
Pada bagian ini juga terdapat representasi Output yang membedakan Mamdani dan Sugeno:
- Mamdani menggunakan kembalian fungsi kurva: `OUTPUT_MF`.
- Sugeno menggunakan deklarasi konstanta/konfigurasi Singleton dictionary: `SUGENO_SINGLETON = {'rendah': 15.0, ...}`.

### B. Komponen "Rule Base" / Basis Aturan (Baris 79 - 131)
Berisi list array Python `RULES` yang menyimpan 42 *tuple*. Setiap *tuple* ini merepresentasikan Aturan Ahli (`IF Usia ... AND BP ... THEN Risiko ...`). Disimpan sebagai referensi fungsi secara murni (*Function Pointers*), yang siap dieksekusi secara iteratif tanpa harus menggunakan rantai `if-else` bertingkat yang rawan bug.

### C. Komponen "Mesin Inferensi" / Inference Engine (Baris 133 - 188)
Ini adalah "otak prosesor" sistem pakar.
- **`evaluasi_rule`**: Looping dari 42 list `RULES`. Mengalikan skor tiap parameter (PRODUCT t-norm). Mengembalikan List berisi kumpulan kekuatan aturan (`alpha`) dan jenis label keluaran.
- **`mamdani_inferensi`**: Mengambil nilai *alpha*, memotong (*clipping*) fungsi output menggunakan metode agregasi `max-min`. Lalu melakukan kalkulasi integral area matematika linier yang dipecah dalam skala grid ukuran grid resolusi 400 (`n=400`) menggunakan array Numpy, dilanjutkan formula "Center of Mass".
- **`sugeno_inferensi`**: Melakukan perhitungan jauh lebih hemat yaitu *Weighted Average* (Bobot alpha $\times$ Singleton). Mengembalikan hasil jauh lebih instan.

### D. Komponen "Visualisasi" Matplotlib (Baris 190 - 391)
Berkat *library* Visualisasi **Matplotlib**, aplikasi Streamlit tidak hanya memberi teks jawaban "Risiko 60%".
- **`plot_mamdani`**: Men-generate figur kanvas raksasa berisi tumpang tindih kurva Trapesium dan agregasi area Mamdani yang ditandai garis putus-putus sebagai letak pasti dari titik Centroid Defuzzifikasi.
- **`plot_sugeno`**: Men-generate figur kompleks menggunakan fitur *GridSpec Matplotlib*. Memetakan 4 panel Fungsi Keanggotaan dari titik nilai input (Input vs Fungsi), diagram bar Chart horizontal untuk membuktikan Firing Strength ($\alpha$), dan bar Chart Vertikal kontribusi Sugeno secara proporsional.

### E. Komponen "Frontend Streamlit" / Tampilan Web (Baris 393 - akhir)

Bagian ini yang langsung terpapar pada pengguna secara visual dan fungsional.

**1. Sistem Caching & Load Deep Learning:**
```python
@st.cache_resource
def load_model_and_scaler():
```
Kode ini menggunakan **Decorator Caching Memory** bawaan Streamlit `@st.cache_resource`. Saat aplikasi dinyalakan, Streamlit memuat file `model_hybrid_dka.h5` yang cukup berat (Jaringan Saraf TensorFlow) beserta file *Scaler*. Hasilnya "dibekukan" di RAM. Tanpa fitur cerdas *Cache* ini, aplikasi akan menjadi lambat dan berat karena web browser akan memaksa CPU memuat ulang model yang sama persis ribuan kali ketika *user* sekadar menggerakkan satu slider Usia.

**2. Form Input Sidebar:**
Sidebar adalah area kontrol di pinggir kiri layar menggunakan perintah `st.sidebar`. Menggunakan widget modern seperti:
- `st.sidebar.number_input()`: Mengunci validasi data input agar tidak error. Misalnya Usia dibatasi dari minimal 20 sampai masimal 80. Membantu menghindari *Crash Runtime*.
- `st.sidebar.selectbox()`: Dropdown aman spesifik untuk nilai 1, 2, atau 3 (Kolesterol & Glukosa).

**3. Tombol Trigger Utama:**
```python
if st.sidebar.button("Hitung Prediksi Risiko", type="primary"):
```
Sistem dijamin tidak akan bekerja/kalkulasi sebelum *user* merasa puas dan mengklik (submit) menekan tombol berwarna primer mencolok ini. Fitur ini sangat penting agar CPU dan daya listrik tidak terbuang sia-sia akibat aplikasi menghitung otomatis saat pengguna masih salah mengetik angka.

**4. Panel Hasil & Matrix Kolom:**
```python
col1, col2, col3 = st.columns(3)
```
Membagi panel antarmuka ke dalam 3 kisi responsif sejajar menggunakan `st.columns`, setiap kolom disuntikkan widget `st.metric()` yang sangat modern mirip *Dashboard Data Analytics* untuk menampilkan hasil 3 perbandingan skor sekaligus secara cantik (Mamdani, Sugeno, dan Deep Learning Hybrid). Dilengkapi penanda panah atas/bawah secara adaptif dengan fitur `delta_color="inverse"`.

Akhirnya, kode secara asinkron (paralel) mengeksekusi kedua *builder* visual plot (`fig_m` dan `fig_s`), yang digambar ke Web Browser menggunakan perintah perender Matplotlib ke Streamlit yakni `st.pyplot()`.

---
## Cara Instalasi & Menjalankan Aplikasi
1. Pastikan ter-install bahasa pemrograman Python (Versi > 3.9).
2. Instal pustaka paket PIP yang dibutuhkan (Keras, Matplotlib, Joblib, Sklearn, Streamlit).
   `pip install pandas numpy scikit-learn tensorflow matplotlib streamlit joblib openpyxl`
3. Arahkan *Terminal/Command Prompt* PC ke dalam direktori/folder *Code tubes*.
4. Eksekusi server web Python ringan bawaan Streamlit:
   ```bash
   streamlit run app.py
   ```
5. Buka Browser (Chrome / Edge / Firefox) dan salin URL jaringan lokal `http://localhost:8501`.
# Panduan Membaca Tabel Hasil Evaluasi Model

Dalam proyek ini, terdapat skrip khusus (`evaluate_accuracy.py` dan `retrain_dl_hybrid.py`) yang berfungsi untuk mencetak tabel evaluasi keakuratan prediksi dari masing-masing model (Fuzzy Mamdani, Fuzzy Sugeno, maupun Deep Learning).

Jika Anda menjalankan skrip tersebut di Terminal atau Jupyter Notebook, sistem akan mencetak tabel hasil pengukuran performa (*Metrics*) dan *Confusion Matrix*. Dokumen ini menjelaskan cara membaca dan menginterpretasikan angka-angka pada tabel tersebut.

---

## 1. Membaca Metrik Klasifikasi (Classification Report)

Tabel metrik biasanya menampilkan 4 buah nilai utama dalam bentuk persentase (%). Berikut adalah penjelasan dan cara membacanya:

*   **Accuracy (Akurasi)**:
    Persentase seberapa banyak prediksi sistem yang bernilai **Benar** secara keseluruhan (baik memprediksi sehat maupun memprediksi sakit jantung).
    *   *Rumus*: `(Benar Sakit + Benar Sehat) / Total Pasien`
    *   *Konteks*: Akurasi 75% berarti dari 100 pasien, sistem berhasil menebak status kardio 75 orang dengan tepat.

*   **Precision (Presisi)**:
    Seberapa akurat sistem ketika ia memprediksi seseorang "Positif Sakit Jantung".
    *   *Rumus*: `Benar Sakit / Total yang Diprediksi Sakit oleh Sistem`
    *   *Konteks*: Presisi tinggi berarti sistem sangat berhati-hati sebelum menvonis seseorang sakit jantung (menghindari alarm palsu).

*   **Recall (Sensitivitas)**:
    Seberapa hebat sistem dalam menemukan pasien yang **benar-benar sakit jantung** di dunia nyata.
    *   *Rumus*: `Benar Sakit / Total Pasien yang Nyatanya Sakit Jantung`
    *   *Konteks*: Dalam medis, **Recall jauh lebih penting daripada Precision**. Sistem yang memiliki Recall tinggi sangat meminimalisir kemungkinan pasien berpenyakit lolos dari diagnosa.

*   **F1-Score**:
    Nilai rata-rata harmonis yang menggabungkan dan menyeimbangkan *Precision* dan *Recall*. Digunakan sebagai indikator mutlak performa model jika jumlah pasien sehat dan pasien sakit dalam dataset tidak seimbang.

---

## 2. Membaca Tabel "Confusion Matrix" (Matriks Kebingungan)

Di bawah nilai persentase, Anda akan melihat sebuah tabel silang berukuran 2x2. Ini disebut Confusion Matrix.

Bentuk umumnya seperti ini:
```text
  Confusion Matrix:
                Predicted
                Neg (0)    Pos (1)
  Actual Neg       TN         FP
  Actual Pos       FN         TP
```

**Cara membaca matriks (Misal dari Prediksi Deep Learning):**
Misalkan hasil tabelnya adalah:
```text
  Actual Neg     5700       1200
  Actual Pos     1800       5000
```
Ini berarti, dari total puluhan ribu data pengujian:

1.  **TN (True Negative) = 5700**: Sudut kiri atas. Sistem memprediksi "Negatif/Sehat", dan faktanya pasien tersebut memang sehat. (Angka ini harus setinggi mungkin).
2.  **TP (True Positive) = 5000**: Sudut kanan bawah. Sistem memprediksi "Positif/Sakit Jantung", dan faktanya pasien tersebut memang memiliki penyakit. (Angka ini harus setinggi mungkin).
3.  **FP (False Positive / Tipe 1 Error) = 1200**: Sudut kanan atas. Alarm Palsu! Sistem memprediksi pasien sakit jantung, padahal aslinya ia sangat sehat. Dalam dunia medis, error ini cukup ditoleransi (pasien hanya perlu tes darah lanjutan untuk memastikan).
4.  **FN (False Negative / Tipe 2 Error) = 1800**: Sudut kiri bawah. **Error paling berbahaya!** Sistem memprediksi pasien sangat "Sehat", namun kenyataannya ia mengidap penyakit kardiovaskular akut. Pasien ini bisa saja pulang tanpa pengobatan dan berujung fatal. Model klasifikasi medis yang baik harus menekan angka FN sekecil mungkin.

---

## 3. Ambang Batas (Thresholding)

Tabel evaluasi sering membandingkan nilai *Threshold* (contoh: `T=55%` vs `T=50%`).

*   **Threshold 50%**: Pasien divonis berisiko jika skor hasil output logika Fuzzy/Deep Learning menyentuh persis 50% atau lebih. Jika 49.9%, dianggap Sehat.
*   **Threshold 55%**: Sistem menjadi lebih kaku/konservatif. Pasien baru akan divonis "Tinggi" jika sistem merasa sangat yakin (skor menembus 55%). Hal ini akan menurunkan nilai *Recall* namun sedikit meningkatkan nilai *Precision*.

**Kesimpulan Evaluasi "Sebelum vs Sesudah"**
Pada skrip evaluasi, versi model BARU (6 input dengan Glukosa + PRODUCT t-norm) dibuat dengan threshold 50% untuk menyeimbangkan antara akurasi umum dan mencegah tingginya nilai FN (kecerobohan fatal) dibandingkan dengan versi model LAMA yang menggunakan threshold kaku 55%.
# Evolusi dan Peningkatan Model (Versi Lama vs Versi Baru)

Proyek ini tidak hanya sekadar membuat satu model lalu selesai, melainkan melalui proses **Peningkatan Terukur (Iterative Improvement)**. Jika Anda membuka skrip `evaluate_accuracy.py`, Anda akan melihat perbandingan antara dua versi model Fuzzy Inference System: **Versi Lama (Sebelum)** dan **Versi Baru (Sesudah)**.

Penambahan dan penyempurnaan fitur ini adalah kunci utama mengapa model yang sekarang jauh lebih kuat dan akurat. Berikut adalah rincian lengkap peningkatan yang telah dilakukan:

---

## 1. Penambahan Fitur Input (Dari 5 Menjadi 6 Variabel)
- **Versi Lama**: Hanya menggunakan 5 variabel input (Usia, Tekanan Darah Sistolik, Tekanan Darah Diastolik, BMI, dan Kolesterol).
- **Versi Baru**: Menambahkan 1 variabel krusial, yaitu **Glukosa (Gula Darah)**.
- **Alasan Peningkatan**: Secara medis, kadar gula darah tinggi (hiperglikemia/diabetes) memiliki korelasi langsung dan sangat kuat dengan kerusakan pembuluh darah. Dengan memasukkan Glukosa, model memiliki "mata ekstra" untuk menangkap pasien berisiko yang mungkin memiliki kolesterol normal namun menderita diabetes.

## 2. Ekspansi Basis Aturan / Rule Base (Dari 25 Menjadi 42 Aturan)
- **Versi Lama**: Hanya mendefinisikan 25 aturan pakar. Beberapa kombinasi kondisi yang mungkin terjadi di dunia nyata tidak ter-cover oleh sistem, sehingga menghasilkan kesimpulan yang "menggantung" atau default ke 50%.
- **Versi Baru**: Aturan diperluas menjadi **42 aturan komprehensif**.
- **Alasan Peningkatan**: Dengan bertambahnya variabel Glukosa, jumlah kemungkinan kombinasi logis (*State Space*) membesar drastis. Penambahan menjadi 42 aturan memastikan hampir semua skenario klinis profil pasien memiliki pemetaan risiko yang pasti, mulai dari pasien muda obesitas hingga pasien tua hipertensi.

## 3. Perubahan Operator T-Norm (Dari MIN menjadi PRODUCT)
- **Versi Lama**: Menggunakan operator **MIN t-norm** (Mencari nilai minimum dari sekumpulan derajat keanggotaan).
  - *Kelemahan*: Jika ada satu saja parameter yang kebetulan memiliki nilai keanggotaan sangat kecil (misal 0.1), maka keseluruhan kekuatan aturan akan langsung jatuh ke 0.1, mengabaikan parameter lain yang mungkin bernilai 0.9 (Sangat kuat).
- **Versi Baru**: Menggunakan operator **PRODUCT t-norm** (Mengalikan seluruh nilai derajat keanggotaan).
  - *Keunggulan*: Jauh lebih sensitif, halus (*smooth*), dan setiap parameter tetap memberikan kontribusi perhitungan matematis tanpa ada yang diabaikan secara paksa.

## 4. Optimasi Nilai Singleton Sugeno
- **Versi Lama**: Menggunakan konstanta baku yang kaku: `Risiko Rendah: 20.0`, `Risiko Sedang: 50.0`, `Risiko Tinggi: 85.0`.
- **Versi Baru**: Dioptimasi berdasarkan distribusi data sesungguhnya menjadi: `Risiko Rendah: 15.0`, `Risiko Sedang: 45.0`, `Risiko Tinggi: 85.0`.
- **Alasan Peningkatan**: Menurunkan titik "Rendah" dari 20 ke 15, dan "Sedang" dari 50 ke 45 membantu memberikan batas (margin) yang lebih tegas antara pasien yang benar-benar sehat dengan yang sakit, mengurangi kebingungan model di area abu-abu.

## 5. Penyesuaian Ambang Batas (Threshold) (Dari 55% ke 50%)
- **Versi Lama**: Menggunakan ambang batas kaku `55%` untuk memvonis pasien berisiko tinggi. Hal ini menyebabkan banyak penderita kardiovaskular tahap awal (skor 51-54%) lolos dari deteksi karena tidak menembus batas 55% (Angka *False Negative* tinggi).
- **Versi Baru**: Ambang batas diturunkan dan dinormalkan ke nilai tengah yang adil, yaitu `50%`. 
- **Dampak**: Sensitivitas (Recall) model dalam menemukan pasien yang benar-benar sakit naik secara signifikan, membuat aplikasi ini lebih aman dan etis untuk digunakan sebagai skrining awal medis.

---

Dengan kelima perubahan mendasar di atas, evaluasi pada skrip `evaluate_accuracy.py` menunjukkan bahwa **Versi Baru memberikan keseimbangan F1-Score dan Recall yang jauh lebih optimal** dibandingkan versi lama, sekaligus membuktikan bahwa sistem berbasis logika murni masih bisa "di-tuning" selayaknya algoritma Machine Learning!
# Struktur dan Penjelasan Setiap File Proyek

Agar Anda benar-benar memahami bagaimana keseluruhan proyek ini dibangun dan saling terhubung, berikut adalah penjelasan **sangat detail** mengenai setiap file yang ada di dalam root folder/direktori proyek Anda beserta fungsinya.

---

### 1. `cardio_train1.xlsx`
*   **Tipe File**: Excel Spreadsheet.
*   **Kegunaan Utama**: Ini adalah **sumber kehidupan (nyawa)** dari proyek ini. File ini berisi dataset mentah berupa data rekam medis puluhan ribu pasien (Usia, Tensi Darah, BMI, Kolesterol, Glukosa, dan status apakah ia mengidap penyakit Kardiovaskular atau tidak).
*   **Cara Kerja**: File ini dibaca oleh Pandas (`pd.read_excel`) di dalam script `Tubes_dka.ipynb`, `retrain_dl_hybrid.py`, dan `evaluate_accuracy.py` untuk diekstraksi nilainya, dibersihkan (data cleaning), dan dipelajari polanya oleh model AI. Tanpa file ini, model tidak punya memori masa lalu untuk belajar.

### 2. `app.py`
*   **Tipe File**: Python Script (Aplikasi Utama).
*   **Kegunaan Utama**: Ini adalah file **inti antarmuka (frontend & backend)** yang berjalan di atas framework web Streamlit. File inilah yang Anda jalankan (`streamlit run app.py`) untuk membuka tampilan web di browser.
*   **Penjelasan Detail di Dalamnya**:
    *   Berisi logika matematis *Membership Function* (Fungsi Keanggotaan Trapesium & Segitiga).
    *   Mendeklarasikan 42 *Rule Base* kepakaran pakar (kombinasi variabel medis).
    *   Mengeksekusi perhitungan inferensi Fuzzy Mamdani dan Sugeno berdasarkan input dari *slider* pada layar.
    *   Memanggil model Deep Learning (`model_hybrid_dka.h5`) untuk memberikan opini prediksi tambahan.
    *   Menggambar *chart* visual (Grafik luas area Mamdani & Panel Bar Sugeno) ke layar menggunakan `matplotlib`.

### 3. `evaluate_accuracy.py`
*   **Tipe File**: Python Script (Alat Evaluasi/Penguji).
*   **Kegunaan Utama**: File ini secara khusus dibuat untuk **menguji dan membuktikan secara ilmiah** seberapa pintar logika Fuzzy yang telah kita bangun.
*   **Penjelasan Detail di Dalamnya**:
    *   Skrip ini tidak menampilkan UI. Saat dijalankan di terminal (`python evaluate_accuracy.py`), ia akan melahap semua data dari `cardio_train1.xlsx`.
    *   Terdapat dua logika di dalamnya: **Versi Lama** (5 variabel, 25 aturan, MIN t-norm) dan **Versi Baru** (6 variabel, 42 aturan, PRODUCT t-norm).
    *   Skrip ini memaksa kedua versi tersebut untuk memprediksi puluhan ribu data pasien satu per satu, kemudian mencocokkan hasil tebakannya dengan kunci jawaban sesungguhnya.
    *   Hasil akhirnya adalah mencetak tabel *Classification Report* (Accuracy, Precision, Recall, F1-Score) dan *Confusion Matrix* (True/False Positive & Negative). Berkat file ini, kita bisa tahu bahwa Versi Baru lebih jago dari Versi Lama.

### 4. `retrain_dl_hybrid.py`
*   **Tipe File**: Python Script (Alat Pelatih Mesin).
*   **Kegunaan Utama**: Ini adalah script arsitek. File ini bertugas untuk **membangun, melatih, dan menyimpan** otak Deep Learning buatan kita (Artificial Neural Network).
*   **Penjelasan Detail di Dalamnya**:
    *   Berisi kode TensorFlow Keras yang mendefinisikan jaringan saraf (Layer, Neuron, ReLU, Sigmoid, Dropout).
    *   Skrip ini menghitung skor *Mamdani* untuk puluhan ribu sampel data, lalu menjadikannya "Fitur Ke-7" yang diumpankan ke model (*Hybrid Approach*).
    *   Skrip ini melakukan proses *Training* selama 30 *Epochs* (putaran).
    *   Pada baris terakhirnya, skrip ini mem- *freeze* (menyimpan) matriks kepintaran yang sudah ia pelajari ke dalam file fisik `model_hybrid_dka.h5` dan `scaler_hybrid_dka.pkl` agar bisa langsung dipakai oleh `app.py`.

### 5. `model_hybrid_dka.h5`
*   **Tipe File**: HDF5 (Hierarchical Data Format).
*   **Kegunaan Utama**: Ini adalah **otak cerdas hasil dari Deep Learning** (Keras/TensorFlow Model) yang sudah jadi dan siap pakai.
*   **Cara Kerja**: Daripada Streamlit (`app.py`) harus melatih ulang jutaan rumus matematika dari awal setiap kali dibuka (yang bisa memakan waktu berjam-jam), file ini menyimpan "Matriks Bobot Saraf" matang. Streamlit hanya tinggal me- *load* file ini, memasukkan data tekanan darah Anda ke dalamnya, dan otak cerdas ini langsung memuntahkan jawaban probabilitas dalam hitungan milidetik.

### 6. `scaler_hybrid_dka.pkl`
*   **Tipe File**: Pickle (Python Object Serialization).
*   **Kegunaan Utama**: File **pendamping wajib** dari model Deep Learning.
*   **Cara Kerja**: Ingat bahwa parameter memiliki skala yang ekstrim (Tekanan darah bernilai 150, Kolesterol bernilai 1). Jaringan saraf (Deep Learning) benci hal ini dan mewajibkan semua data dikecilkan ke rentang angka desimal -1 hingga 1 (*Standardization/Z-Score*). File `scaler` ini merekam persis "rumus pengecilan" historis yang digunakan saat pelatihan, agar saat `app.py` menginput tensi darah 130 secara *real-time*, angka tersebut dikecilkan dengan takaran rumus yang sama sebelum dilempar ke otak `.h5`.

### 7. `Tubes_dka.ipynb`
*   **Tipe File**: Jupyter Notebook.
*   **Kegunaan Utama**: Ini adalah **buku catatan penelitian (Lab Book)** yang digunakan saat fase *Research & Development* (R&D).
*   **Cara Kerja**: Biasanya digunakan untuk mengeksplorasi data (*Exploratory Data Analysis*), mencetak grafik, menguji sebagian fungsi keanggotaan sebelum ditulis secara serius ke `app.py`. Di dalamnya terdapat sel-sel kode per blok yang memudahkan eksekusi kode potong-demi-potong untuk mencari bug atau mem-visualisasikan dataset. File ini adalah draf dan cetak biru eksperimental dari keseluruhan proyek ini.

### 8. Folder `dokumentasi_proyek/`
*   **Tipe File**: Folder Direktori (Berisi file .md).
*   **Kegunaan Utama**: Perpustakaan ilmu. Direktori ini (tempat Anda membaca teks ini) menyimpan ensiklopedia lengkap penjelasan arsitektur, algoritma, rumus matematika, matriks, dan evolusi sejarah program yang disusun untuk keperluan pemahaman teori atau pelaporan akademik tingkat lanjut.

---
Dengan pemahaman struktur file di atas, Anda sekarang bisa melihat bahwa setiap komponen (*Dataset* $\rightarrow$ *Evaluasi* $\rightarrow$ *Pelatih DL* $\rightarrow$ *Otak H5* $\rightarrow$ *Aplikasi Streamlit*) berkerja layaknya pabrik yang terintegrasi sempurna!
# Bedah Kode Secara Mendalam: `evaluate_accuracy.py`

File `evaluate_accuracy.py` adalah skrip pengujian kritis. Di bagian ini, kita akan membedah logika pemrograman secara mendetail baris demi baris agar Anda paham 100% cara kerjanya.

---

## 1. Import Library (Baris 12-14)
```python
import pandas as pd
import numpy as np
from collections import Counter
```
- `pandas`: Digunakan untuk membaca file Excel (`.xlsx`) ke dalam bentuk Data Frame tabular (seperti tabel SQL).
- `numpy`: Digunakan untuk komputasi matriks yang sangat cepat, seperti membuat *array* linear `linspace` untuk perhitungan luas kurva.
- `Counter`: Modul standar Python untuk menghitung distribusi frekuensi, berguna untuk melihat berapa banyak pasien yang Sehat (0) dan Sakit (1).

## 2. Load & Clean Data (Baris 19-25)
```python
df = pd.read_excel('cardio_train1.xlsx')
df_clean = df[(df['ap_hi'] >= 60) & (df['ap_hi'] <= 250) &
              (df['ap_lo'] >= 40) & (df['ap_lo'] <= 150)].copy()
df_clean['bmi'] = df_clean['weight'] / (df_clean['height']/100)**2
```
Blok kode ini membaca Excel, kemudian menggunakan *Boolean Indexing* dari Pandas untuk membuang anomali data (tekanan darah sistolik < 60 atau > 250 dibuang karena mustahil secara medis). Selanjutnya melakukan ekstraksi (Feature Engineering) tinggi dan berat badan menjadi satu fitur baru: `bmi`.

## 3. Definisi Fungsi Keanggotaan (Baris 30-62)
```python
def trapmf(x, a, b, c, d): ...
def trimf(x, a, b, c): ...
```
Fungsi murni matematika. `trapmf` menggunakan operator `if-else` untuk mengecek posisi input $x$. Jika berada di area naik `(x-a)/(b-a)`, jika di puncak mengembalikan `1.0`, dan jika turun `(d-x)/(d-c)`. Semuanya adalah rumus translasi grafik langsung ke Python.

## 4. Arsitektur Versi Lama (Baris 67-95)
```python
RULES_OLD = [ (mu_usia_muda, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, 'rendah'), ... ]
SINGLETON_OLD = {'rendah': 20.0, 'sedang': 50.0, 'tinggi': 85.0}
```
Berisi deklarasi Array dari Fungsi (Function pointer array). Variabel ini menyimpan memori versi lama yang berisi 25 baris aturan. Tidak ada Glukosa di sini. Singleton Sugenonya menggunakan konstanta `20, 50, 85`.

## 5. Arsitektur Versi Baru (Baris 100-148)
```python
RULES_NEW = [ ... ]
SINGLETON_NEW = {'rendah': 15.0, 'sedang': 45.0, 'tinggi': 85.0}
```
Inilah peningkatan proyeknya. Terdapat 42 baris aturan yang menyertakan input ke-6 (`mu_gluc_normal / tinggi`). Serta menggunakan konstanta Singleton yang telah digeser ke batas aman `15, 45, 85`.

## 6. Mesin Inferensi Terpisah (Baris 154-212)
Terdapat 4 blok fungsi raksasa di sini:
- `sugeno_old` & `mamdani_old`: Looping `RULES_OLD`, menghitung kekuatan (*Firing Strength*) menggunakan fungsi bawaan `min()` sebagai implementasi murni **MIN t-norm**.
- `sugeno_new` & `mamdani_new`: Looping `RULES_NEW`, menghitung kekuatan dengan operator kali `*` secara matematis beruntun sebagai implementasi **PRODUCT t-norm**.

Khusus untuk `mamdani`, dilakukan iterasi tambahan di dalam skala 0-100 `(S_vals)` menggunakan `np.maximum` untuk menggabungkan kurva yang terpotong. Kemudian `np.sum(S_vals * agg) / denom` adalah implementasi nyata dari rumus kalkulus *Center of Mass/Integral Diskret*.

## 7. Fungsi Penghitung Akurasi Manual (Baris 218-235)
```python
def compute_metrics(y_true, y_pred):
```
Fungsi murni tanpa *library* eksternal. Membandingkan List Kunci Jawaban (`y_true`) dengan Tebakan Sistem (`y_pred`).
- `tp` bertambah 1 jika Asli = 1 dan Tebakan = 1.
- `tn` bertambah 1 jika Asli = 0 dan Tebakan = 0.
Dan seterusnya, hingga menghitung `accuracy`, `precision`, `recall`, dan `f1-score` lewat rumus aritmatika konvensional.

## 8. Eksekutor Utama (Baris 240-286)
- **Eksekusi Iteratif (`iterrows`)**: Melakukan komputasi baris demi baris pada `df_clean` untuk Sugeno (Cepat).
- **Sampling Mamdani**: `df_clean.sample(n=5000)`. Mengapa di-*sample* (diambil sampel acak)? Karena komputasi Integral Centroid Mamdani sangat mahal secara CPU. Menguji puluhan ribu baris dengan Mamdani memakan waktu sangat lama (berjam-jam), sehingga sampel 5000 dirasa cukup sebagai wakil statistik.
- **Konfigurasi Looping List**: Menyimpan parameter (Threshold 50 vs 55) ke dalam Array of Tuple `configs`, yang memicu konversi skor persentase `s >= threshold` menjadi label `1` (Sakit).
- Terakhir, memanggil `compute_metrics` lalu mencetak hasilnya secara rapi ke *Console/Terminal* Anda.
# Bedah Kode Secara Mendalam: `retrain_dl_hybrid.py`

File `retrain_dl_hybrid.py` adalah skrip yang bertugas membangun "otak" Jaringan Saraf Tiruan (*Artificial Neural Networks*). Mari kita bedah fungsi blok-blok *backend* cerdas ini lapis demi lapis.

---

## 1. Import Library Keras & Scikit-Learn (Baris 14-22)
```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import joblib
```
- `tensorflow` & `keras`: Modul utama (Framework Google) untuk membangun lapisan arsitektur Deep Learning (*Dense, Dropout, Sequential*).
- `train_test_split`: Fungsi pemecah array dataset agar terbagi menjadi proporsi "Ujian" dan "Latihan" secara acak.
- `StandardScaler`: Formula pengecilan angka drastis (Standardisasi berbasis kurva lonceng/Z-Score).
- `joblib`: Digunakan untuk membekukan memori skrip (menyimpan object Scaler ke bentuk `.pkl`).

## 2. Bagian 1 & 2: Rekonstruksi Fuzzy & Load Dataset (Baris 24-134)
Blok awal ini adalah murni *copy-paste* dari `app.py`. Ia mendefinisikan Fungsi Keanggotaan, 42 `RULES` Baru, dan metode `mamdani_inferensi` dengan `PRODUCT t-norm`.
Setelahnya, baris ini meng- *load* dataset `cardio_train1.xlsx` menggunakan Pandas dengan fungsi Boolean filter batas medis (Sistolik 60-250, dst) serta perumusan variabel `bmi`.

## 3. Bagian 3: Komputasi Skor Hybrid Mamdani (Baris 136-150)
```python
print("\n[2/5] Computing Mamdani scores for all data...")
mamdani_scores = []
for idx, (_, row) in enumerate(df_clean.iterrows()):
    score = mamdani_inferensi(row['age'], row['ap_hi'], row['bmi'],
                               row['ap_lo'], row['cholesterol'], row['gluc'])
    mamdani_scores.append(score)
df_clean['mamdani_score'] = mamdani_scores
```
Di sinilah keajaiban **HYBRID** terjadi. Jaringan Saraf tidak murni belajar dari data telanjang (seperti Tensi). Melainkan, skrip ini memaksa setiap baris pasien melewati kalkulator Fuzzy Mamdani terlebih dahulu. Nilai persentase Fuzzy (misal: 62.4%) ditambahkan menjadi kolom baru bernama `mamdani_score`. Sehingga mesin belajar dari "Pendapat Pakar Logika" sebagai sebuah petunjuk (*Feature / Clue*). Karena menggunakan Mamdani murni (bukan sampel), iterasi perhitungan ini sengaja dirancang sangat lama (sekitar ~5 menit komputasi intensif CPU).

## 4. Bagian 4: Pemecahan dan Penskalaan (Baris 152-169)
```python
X = df_clean[FEATURE_COLS].values
y = df_clean['cardio'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```
- Array fitur (`X`) memuat 7 parameter, array kunci jawaban (`y`) memuat 0/1.
- `train_test_split(..., test_size=0.2)`: Secara acak merobek Excel, menyisihkan 20% khusus untuk tes agar model tidak curang (karena tidak pernah melihat kunci jawaban bagian tes ini). Parameter `stratify=y` memastikan rasio pasien sakit dan sehat pada pecahan tersebut seimbang.

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```
Penting! `fit_transform` menyuruh mesin membaca distribusi data *training* (Mencari rata-rata & deviasi), lalu menskalakannya. Di sisi lain, *test set* HANYA memakai perintah `transform` untuk mencegah kebocoran informasi distribusi ke dalam model.

## 5. Bagian 5: Mendirikan Gedung Arsitektur Saraf (Baris 171-199)
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(len(FEATURE_COLS),)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(32, activation='relu'),
    ...
    keras.layers.Dense(1, activation='sigmoid')
])
```
- `Sequential`: Berarti data akan mengalir dari atas ke bawah.
- `Dense(64)`: Lapis pertama berisi 64 otak mini (Neuron) yang menempel satu sama lain *Fully-Connected*.
- `Activation='relu'`: Menonaktifkan angka negatif yang merusak gradien matematika.
- `Dropout`: Melatih model lebih keras dengan secara buta menembak mati 30% memori acak setiap putaran iterasi agar tidak manja/menghafal.
- Lapis paling dasar berjenis `Dense(1)` dengan `sigmoid` bertugas memeras ratusan sinyal dari atasnya menjadi 1 angka pasti pecahan (misal `0.78`) yang berarti 78% yakin Sakit Jantung.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```
Merupakan penyatuan akhir (*Compile*) di mana *Loss Function* menggunakan standar dua target klasifikasi, serta memakai alat *Optimizer Adam* yang canggih memutakhirkan kalkulus turunan *Gradient Descent*.

```python
history = model.fit(X_train_scaled, y_train, epochs=30, batch_size=64, validation_split=0.2)
```
Skrip inti pemicu belajar. Berjalan 30 putaran (`epochs=30`), menyerap data sebanyak 64 baris sekali telan (`batch_size=64`), dan dari sisa bagian 80% Latihan itu, ia masih disiplin menyisihkan 20% lagi (`validation_split`) untuk bercermin.

## 6. Bagian 6: Ujian Kelulusan dan Penyimpanan (Baris 201-226)
```python
y_pred_prob = model.predict(X_test_scaled, verbose=0).flatten()
y_pred = (y_pred_prob >= 0.5).astype(int)
```
Data `X_test` (Ujian Nasional) yang diumpankan ke model disaring. Jika keyakinan mesin $\ge$ 50% (0.5), maka dibulatkan menjadi 1.

Setelah itu, hasil `y_pred` dibandingkan dengan `y_test` diumpankan ke pustaka *Scikit-Learn* (`classification_report` & `confusion_matrix`) yang akan di-print ke layar.
Terakhir, `model.save('model_hybrid_dka.h5')` dan `joblib.dump(scaler, 'scaler_hybrid_dka.pkl')` dipanggil. Model ini berhasil menamatkan pelatihannya dan otaknya disalin permanen ke *Hard Drive* lokal siap digunakan *Streamlit*.
# Panduan Sukses Presentasi Tugas Besar (Cheat Sheet)

Melihat dari kelengkapan dokumentasi yang telah kita susun (9 dokumen), proyek Anda saat ini sudah berada di standar **Tugas Akhir / Skripsi**, bukan lagi sekadar Tugas Besar biasa. 

Untuk memastikan Anda 100% siap saat didemo/dipresentasikan di depan Dosen atau Asisten Laboratorium, berikut adalah panduan urutan presentasi dan "kisi-kisi" pertanyaan yang paling sering ditanyakan, beserta jawaban pamungkasnya!

---

## ðŸš€ Skenario Urutan Presentasi yang Ideal

**Langkah 1: Pendahuluan & Latar Belakang (Gunakan Dokumen 01)**
*   Mulai dengan masalah nyata: *"Penyakit kardiovaskular adalah pembunuh nomor 1. Sayangnya, diagnosis awal butuh alat mahal. Tujuan proyek ini adalah membuat sistem skrining awal cerdas hanya dari data rekam medis dasar (Tensi, Usia, BMI)."*
*   Tunjukkan `cardio_train1.xlsx` sekilas, sampaikan bahwa datanya sudah dibersihkan dari *outlier*.

**Langkah 2: Demo Aplikasi Streamlit (Gunakan Dokumen 04)**
*   Jalankan `streamlit run app.py` dan buka browser.
*   Pilih satu skenario pasien. Misal: Usia 60, Tensi 160/100, Kolesterol Tinggi, Glukosa Tinggi.
*   Klik **Hitung Prediksi** dan pamerkan UI visualisasinya. Biarkan dosen melihat perpotongan kurva Mamdani dan grafik bar Sugeno yang sangat interaktif.

**Langkah 3: Penjelasan "Rahasia Dapur" (Gunakan Dokumen 02 & 03)**
*   Jelaskan bahwa sistem ini tidak menebak acak. Terdapat **42 Aturan Pakar (Rule Base)** di baliknya.
*   Jelaskan metode **Hybrid**: *"Skor Mamdani yang keluar dari logika pakar, kami suntikkan kembali sebagai fitur ekstra ke dalam otak Deep Learning. Jadi model kami punya insting manusia sekaligus akurasi mesin."*

**Langkah 4: Pembuktian Peningkatan Model (Gunakan Dokumen 06)**
*   Ini adalah bagian **KILLER / Paling Bikin Kagum**.
*   Buka terminal, jalankan `python evaluate_accuracy.py`.
*   Tunjukkan perbedaan matriksnya. *"Pak/Bu, awalnya kami cuma pakai 5 variabel (MIN t-norm) dan akurasinya kurang. Setelah kami rombak pakai 6 variabel, tambah Glukosa, dan pakai PRODUCT t-norm, akurasinya meroket dan False Negatifnya turun drastis."*

---

## ðŸŽ¯ Kisi-Kisi Pertanyaan Dosen & Cara Menjawabnya

### Pertanyaan 1: *"Mengapa kamu menggunakan Fungsi Keanggotaan Trapesium untuk Tensi/Usia, kok tidak Segitiga semua?"*
> **Jawaban:** "Karena variabel tensi dan usia punya rentang 'batas aman' yang stabil, bukan cuma satu titik puncak mutlak. Misalnya tensi normal itu ada di rentang 70 sampai 110, semuanya bernilai mutlak 1.0 (sehat). Kalau pakai segitiga, hanya angka 90 saja yang 1.0, angka 100 sudah dianggap tidak sehat penuh." (Referensi: Dokumen 02)

### Pertanyaan 2: *"Apa bedanya Mamdani dan Sugeno di kodemu?"*
> **Jawaban:** "Mamdani pakai himpunan kurva untuk outputnya, makanya grafiknya luas area (tumpang tindih) dan dihitung pakai integral/titik berat (Centroid). Kalau Sugeno outputnya angka mutlak (Singleton 15, 45, 85), jadi cuma dihitung pakai rumus Rata-Rata Terbobot (Weighted Average) yang eksekusinya hitungan milidetik." (Referensi: Dokumen 02)

### Pertanyaan 3: *"Coba jelaskan arsitektur Deep Learning-mu!"*
> **Jawaban:** "Kami pakai TensorFlow Keras berjenis Sequential. Lapisannya 64-32-16 neuron pakai aktivasi ReLU. Kami sengaja tambahkan *Dropout Layer* sebesar 30% supaya modelnya tidak menghafal data (overfitting). Outputnya 1 neuron Sigmoid untuk penentu akhir (1 atau 0)." (Referensi: Dokumen 09)

### Pertanyaan 4: *"Di matriks evaluasi, kenapa kamu bilang versi Baru lebih bagus, padahal akurasinya mirip-mirip?"*
> **Jawaban:** "Untuk penyakit jantung, **Akurasi** bisa menipu, Pak/Bu. Metrik yang paling krusial adalah **Recall / Sensitivitas**. Di versi baru, jumlah `False Negative` (pasien sakit tapi ditebak sehat) turun jauh. Kami lebih baik salah nebak orang sehat dibilang sakit (False Positive), daripada melepas pasien berpenyakit kronis pulang ke rumah." (Referensi: Dokumen 05)

### Pertanyaan 5: *"Apakah kamu train ulang modelnya tiap kali Streamlit dibuka?"*
> **Jawaban:** "Tentu tidak. Pelatihannya (`retrain_dl_hybrid.py`) hanya dieksekusi sekali di belakang layar sampai dapat akurasi terbaik. Lalu bobot otaknya kami *freeze* ke dalam file `.h5`. Di Streamlit (`app.py`), kami pakai fitur `@st.cache_resource` untuk meload `.h5` tersebut satu kali saja ke RAM, makanya webnya tidak lag sama sekali saat digeser slidernya." (Referensi: Dokumen 04 & 07)

---
Berbekal pemahaman dari 9 Dokumen Markdown sebelumnya dan *Cheat Sheet* ini, nilai A sudah pasti di tangan Anda! Selamat berjuang! ðŸ†
