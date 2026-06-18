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
