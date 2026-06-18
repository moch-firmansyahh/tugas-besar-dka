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
*   **Cara Kerja**: Ingat bahwa parameter memiliki skala yang ekstrim (Tekanan darah bernilai 150, Kolesterol bernilai 1). Jaringan saraf (Deep Learning) benci hal ini dan mewajibkan semua data dikecilkan ke rentang angka desimal -1 hingga 1 (*S
tandardization/Z-Score*). File `scaler` ini merekam persis "rumus pengecilan" historis yang digunakan saat pelatihan, agar saat `app.py` menginput tensi darah 130 secara *real-time*, angka tersebut dikecilkan dengan takaran rumus yang sama sebelum dilempar ke otak `.h5`.

### 7. `Tubes_dka.ipynb`
*   **Tipe File**: Jupyter Notebook.
*   **Kegunaan Utama**: Ini adalah **buku catatan penelitian (Lab Book)** yang digunakan saat fase *Research & Development* (R&D).
*   **Cara Kerja**: Biasanya digunakan untuk mengeksplorasi data (*Exploratory Data Analysis*), mencetak grafik, menguji sebagian fungsi keanggotaan sebelum ditulis secara serius ke `app.py`. Di dalamnya terdapat sel-sel kode per blok yang memudahkan eksekusi kode potong-demi-potong untuk mencari bug atau mem-visualisasikan dataset. File ini adalah draf dan cetak biru eksperimental dari keseluruhan proyek ini.

### 8. Folder `dokumentasi_proyek/`
*   **Tipe File**: Folder Direktori (Berisi file .md).
*   **Kegunaan Utama**: Perpustakaan ilmu. Direktori ini (tempat Anda membaca teks ini) menyimpan ensiklopedia lengkap penjelasan arsitektur, algoritma, rumus matematika, matriks, dan evolusi sejarah program yang disusun untuk keperluan pemahaman teori atau pelaporan akademik tingkat lanjut.

---
Dengan pemahaman struktur file di atas, Anda sekarang bisa melihat bahwa setiap komponen (*Dataset* $\rightarrow$ *Evaluasi* $\rightarrow$ *Pelatih DL* $\rightarrow$ *Otak H5* $\rightarrow$ *Aplikasi Streamlit*) berkerja layaknya pabrik yang terintegrasi sempurna!
