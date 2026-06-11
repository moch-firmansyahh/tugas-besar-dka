# Penjelasan Lengkap Source Code & Update Sistem (Tubes DKA)

Dokumen ini membedah secara lengkap setiap bagian dari *source code* dan *Streamlit Web App* untuk keperluan presentasi dan tanya jawab dosen. Terutama berfokus pada pembaruan terakhir yang digunakan untuk mencapai akurasi tertinggi dan mendapatkan poin bonus maksimal (GUI Streamlit + Deep Learning).

---

## BAGIAN 1: PEMBARUAN SISTEM (REVISI FINAL)
Pada revisi ini, kita melakukan *tuning* besar-besaran untuk memaksimalkan akurasi Fuzzy, serta membuat antarmuka (GUI) interaktif.

1. **Penambahan Fitur (Input):**
   - Sebelumnya hanya 5 input, sekarang menjadi **6 input** dengan ditambahkannya **Glukosa** (Normal, Tinggi, Sangat Tinggi).
2. **Perluasan Basis Aturan (Rule Base):**
   - Aturan IF-THEN diperluas dari 25 menjadi **42 aturan** untuk mencakup peran tingkat Glukosa dan pembagian tekanan darah yang lebih spesifik.
3. **Operator Logika Fuzzy AND (T-Norm):**
   - **PENTING:** Operator AND diubah dari metode `MIN()` menjadi `PRODUCT()` (perkalian).
   - *Alasan untuk Dosen:* "Penggunaan metode Product memberikan nilai derajat kebenaran (*firing strength*) yang lebih sensitif dan mulus (*smooth*) dibandingkan Min yang memotong kaku. Hal ini terbukti secara empiris menaikkan akurasi dari ~66% menjadi 68.5%."
4. **Tuning Konstanta Sugeno (*Singletons*):**
   - Nilai keluaran Sugeno disesuaikan berdasarkan kalibrasi data:
     - Rendah = 15
     - Sedang = 45
     - Tinggi = 85
5. **Aplikasi Web Terintegrasi (Streamlit):**
   - Mendapatkan **Bonus +5 Poin** dengan membuat *dashboard* interaktif yang bisa langsung digunakan oleh *user* tanpa perlu menjalankan cell Jupyter Notebook.

---

## BAGIAN 2: FUZZY INFERENCE SYSTEM (FIS)

### 1. Deklarasi Fungsi Keanggotaan (Membership Function)
Kita tidak menggunakan library bawaan (seperti `scikit-fuzzy`), melainkan mendefinisikan fungsinya dari awal (*from scratch*):
- `trapmf(x, a, b, c, d)`: Membentuk kurva berbentuk Trapesium. 
- `trimf(x, a, b, c)`: Membentuk kurva berbentuk Segitiga. Memiliki titik puncak tunggal pada $b$.

### 2. Evaluasi Rule (Aturan Logika)
Fungsi `evaluasi_rule_v2` bekerja dengan:
- Menghitung derajat kecocokan (`alpha`) untuk setiap kombinasi input.
- Menggunakan operator **AND** berbasis perkalian (`PRODUCT`). Contoh: Jika rule berbunyi "Muda (0.8) DAN Hipertensi (0.5)", maka kekuatannya adalah $0.8 \times 0.5 = 0.4$.

### 3. Inferensi Mamdani & Defuzzifikasi Centroid
1. **Implikasi (Clipping):** Memotong atap kurva output berdasarkan nilai `alpha` dari rule yang aktif.
2. **Agregasi:** Menggabungkan semua kurva output yang terpotong menjadi satu luasan baru menggunakan fungsi maksimum (`np.maximum`).
3. **Defuzzifikasi:** Mencari "titik berat" (Centroid) dari luasan menggunakan integral numerik.

### 4. Inferensi Sugeno & Weighted Average
- Sistem mengalikan `alpha` tiap rule yang aktif dengan nilai konstanta outputnya (*singleton*).
- Mencari rata-ratanya menggunakan **Weighted Average** (Nilai Total / Total Bobot Alpha).
- *Alasan untuk Dosen:* "Sugeno komputasinya jauh lebih ringan dan cepat dibandingkan Mamdani karena tidak memerlukan perhitungan integral, sangat cocok untuk sistem *real-time*."

---

## BAGIAN 3: HYBRID NEURO-FUZZY (DEEP LEARNING)

Mendapatkan **Bonus +20 Poin** dengan mengintegrasikan Fuzzy dan Deep Learning secara bersamaan.

- **Syarat Terpenuhi:** DL tidak menggantikan Fuzzy. DL justru bertindak sebagai asisten cerdas yang memproses data mentah + hasil dari Fuzzy.
- **Input Model (7 Fitur):** `Usia`, `Tekanan Sistolik`, `Tekanan Diastolik`, `BMI`, `Kolesterol`, `Glukosa`, dan **`Skor Mamdani`**.
- **Arsitektur:** *Multi-Layer Perceptron (Keras)*: `Dense(64)` $\rightarrow$ `Dropout(0.3)` $\rightarrow$ `Dense(32)` $\rightarrow$ `Dropout(0.2)` $\rightarrow$ `Dense(16)` $\rightarrow$ `Dense(1, sigmoid)`.
- **Hasil:** Akurasi meningkat drastis menjadi **~72.89%** (dibandingkan Fuzzy saja yang berada di angka ~68%).

**Key Takeaways untuk Dosen:**
> *"Kenapa pakai Hybrid?"*
> "Fuzzy Inference System memberikan **transparansi (White-Box)**, logikanya dapat divalidasi langsung oleh dokter. Namun batas klasifikasinya statis. Oleh karena itu, kita memasukkan skor Fuzzy tersebut ke dalam Deep Learning **(Black-Box)** agar mesin bisa mencari celah akurasi yang lebih presisi berdasarkan probabilitas dari puluhan ribu data nyata pasien."

---

## BAGIAN 4: CARA MEMBACA DASHBOARD (GRAFIK STREAMLIT)

Aplikasi kita menampilkan visualisasi perhitungan yang sangat transparan. Jika diminta mendemokan:

### 1. Visualisasi Proses Fuzzy (Mamdani)
* **Grafik Agregasi & Defuzzifikasi (Kurva Trapesium Penuh):**
  - **Area Biru Muda/Gelap:** Ini adalah gabungan (agregasi) dari semua keputusan aturan yang aktif. Bagian atapnya yang datar menandakan kurva tersebut "terpotong" oleh nilai $\alpha$ (firing strength).
  - **Garis Putus-putus Vertikal:** Ini adalah letak jatuhnya "Titik Berat" (Centroid) dari area gabungan tadi. Angka di sebelah garis putus-putus tersebut (misal: `42.1%`) adalah persentase murni risiko pasien dari metode Mamdani.

### 2. Visualisasi Proses Fuzzy (Sugeno)
Dashboard ini memiliki **8 Panel (Subplots)** yang membedah proses di balik layar:
* **Panel 1 - 6 (Fungsi Keanggotaan):** 
  - Menampilkan kurva batas Usia, Tekanan Darah, BMI, Kolesterol, dan Glukosa.
  - **Garis Merah Putus-putus:** Menunjukkan "di mana" posisi input pasien secara persis berada. Kamu bisa melihat apakah pasien lebih dominan masuk kategori "Normal" atau "Tinggi" dari perpotongannya.
* **Panel 7 (Kekuatan Aturan Aktif / Firing Strength):**
  - Ini adalah *Bar Chart Horizontal*.
  - Baris R13, R14, dll menunjukkan Aturan (Rule) mana saja yang "terpantik" (menyala) oleh kondisi pasien.
  - Semakin panjang baloknya, semakin besar pengaruh aturan tersebut. Warnanya menunjukkan rekomendasi aturan itu (Biru = Rendah, Hijau = Sedang, Kuning = Tinggi).
* **Panel 8 (Kontribusi Prediksi Sugeno):**
  - Ini adalah *Bar Chart Vertikal*.
  - Menunjukkan kontribusi nyata secara matematis ($\alpha \times z$).
  - **Garis Merah Putus-putus Horizontal:** Menunjukkan letak nilai akhir prediksi Sugeno (*Weighted Average*) yang diambil dari perbandingan balok-balok di bawahnya.
  
### 3. Grafik Hasil Evaluasi (Jika mendemokan Jupyter Notebook)
* **Confusion Matrix (Kotak Warna Biru/Merah):**
  - **Kiri Atas (True Negative):** Pasien SEHAT yang sukses ditebak SEHAT.
  - **Kanan Bawah (True Positive):** Pasien SAKIT yang sukses ditebak SAKIT.
  - **Kiri Bawah (False Negative):** Paling berbahaya secara medis! Pasien sakit tapi dibilang sehat. (Kita menggunakan Tuning dan Deep Learning untuk menekan angka di kotak ini sekecil mungkin).
* **Learning Curves (Grafik Garis DL):**
  - Garis *Loss* harus turun, *Accuracy* harus naik. Jika jarak antara garis Train (Biru) dan Validation (Oranye) sangat jauh, artinya model *Overfitting* (cuma menghafal jawaban). Model kita memiliki jarak yang dekat, membuktikan model kita cerdas dan *robust*.
