# 🫀 Dokumentasi Proyek: Deteksi Risiko Kardiovaskular (Fuzzy & Deep Learning)

Selamat datang di direktori dokumentasi proyek! Folder ini memuat penjelasan **SANGAT LENGKAP 100%** mengenai segala aspek yang terkait dengan alur algoritma, data, dan program antarmuka dari Tugas Besar / Proyek ini.

Dokumentasi ini ditulis sebagai panduan komprehensif dari hulu ke hilir. Silakan klik tautan pada daftar isi di bawah ini untuk membaca masing-masing topik.

---

## 📑 Daftar Isi Dokumentasi Utama

### 1. 📊 [Penjelasan Dataset & Preprocessing](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/01_Penjelasan_Dataset.md)
Membahas asal usul data rekam medis pasien (`cardio_train1.xlsx`), bagaimana cara membersihkan data dari nilai tak masuk akal (Outlier), rumus BMI, dan pemahaman terkait masing-masing dari ke-6 fitur input yang digunakan (Usia, Tensi, dsb).

### 2. 🧠 [Logika Fuzzy: Mamdani dan Sugeno secara Mendalam](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/02_Fuzzy_Logic_Sugeno_dan_Mamdani.md)
Membahas konsep utama pemodelan kepakaran medis ke dalam bahasa mesin. Mencakup rumus matematika pembentuk Fungsi Keanggotaan, evaluasi 42 Aturan (Rule Base) dengan *Product T-Norm*, serta perbedaan mendasar kalkulasi persentase antara metode integral Mamdani (*Centroid*) melawan perhitungan *Weighted Average* Sugeno.

### 3. 🤖 [Arsitektur Deep Learning Hybrid Terperinci](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/03_Deep_Learning_Hybrid.md)
Membahas topologi arsitektur Machine Learning (Jaringan Saraf Tiruan) yang di-training pada proyek ini. Mencakup pemahaman fitur tambahan *Hybrid*, fungsi aktivasi *ReLU/Sigmoid*, metode pencegah overfitting (*Dropout*), hingga nilai *Hyperparameter* selama pelatihan (*Adam Optimizer, Epoch, Batch size*).

### 4. 💻 [Penjelasan Antarmuka Web (Streamlit App)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/04_Penjelasan_Streamlit_App.md)
Membedah arsitektur kode file `app.py` yang dibangun di atas framework web Streamlit. Menjelaskan secara berurutan mulai dari manajemen memori (Caching), penataan sidebar input, tombol kalkulasi, hingga teknik render grafik kanvas menggunakan *Matplotlib*.

### 5. 📈 [Panduan Membaca Tabel Hasil Evaluasi Model](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/05_Penjelasan_Tabel_Evaluasi.md)
Penjelasan khusus tentang metrik ukur performa model. Membahas *Accuracy, Precision, Recall, F1-Score* secara konteks medis, serta menjabarkan tabel *Confusion Matrix* (True Negative, False Negative, dll).

### 6. 🚀 [Evolusi dan Peningkatan Model (Versi Lama vs Baru)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/06_Evolusi_dan_Peningkatan_Model.md)
Bagian paling kritikal yang menjabarkan **mengapa model saat ini diklaim jauh lebih baik**. Membahas transisi evolusi proyek dari sekadar menggunakan 5 Variabel Input dan 25 Aturan, diekspansi menjadi 6 Input (Glukosa) + 42 Aturan, serta perubahan nilai ambang batas (*Thresholding*).

### 7. 📁 [Struktur dan Penjelasan Setiap File Proyek](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/07_Struktur_dan_Penjelasan_File_Proyek.md)
*Master guide* dari seluruh direktori proyek! Membedah satu per satu setiap *script* `.py`, *file* konfigurasi, model `.h5`, dan data `.xlsx` yang ada di luar folder ini, serta mengupas tuntas keterkaitannya satu sama lain layaknya sebuah anatomi program yang utuh.

### 8. 🔍 [Bedah Kode Secara Mendalam: evaluate_accuracy.py](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/08_Penjelasan_Kode_evaluate_accuracy.md)
Khusus bagi Anda yang butuh rincian spesifik mengenai *coding*, dokumen ini menjelaskan kode python per blok. Penjelasan mencakup deklarasi Array `RULES`, eksekusi iteratif `iterrows`, dan algoritma manual pembentukan tabel Akurasi dan Presisi.

### 9. 🧠 [Bedah Kode Secara Mendalam: retrain_dl_hybrid.py](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/09_Penjelasan_Kode_retrain_dl.md)
Membongkar baris demi baris rahasia di balik otak TensorFlow. Dokumen ini menjelaskan rinci bagaimana data dari Excel di-potong menggunakan `train_test_split`, disterilkan menggunakan `StandardScaler`, dimasukkan kalkulator *Hybrid Mamdani*, sebelum diolah paksa ke dalam matriks Jaringan Saraf `Dense`!

### 10. 🏆 [Panduan Sukses Presentasi Tugas Besar (Cheat Sheet)](file:///c:/Users/Firman/Documents/Kuliah/Tugas%20kuliah/Semester%204/Dka/Code%20tubes/dokumentasi_proyek/10_Panduan_Presentasi_Tugas_Besar.md)
**Wajib BACA Sebelum Demo!** Dokumen penutup ini tidak lagi membahas teori, melainkan taktik *Public Speaking*. Berisi skenario urutan presentasi dari awal sampai akhir, serta bocoran "Kisi-Kisi Pertanyaan Maut" yang sering dilontarkan Dosen Penguji beserta contekan kunci jawabannya.

---

> [!TIP]
> **Cara Membaca Terbaik**: Sangat disarankan untuk membaca urutan dokumen di atas secara berurutan dari nomor 1 hingga nomor 6 agar mendapatkan pemahaman logika komputasi yang nyambung dan tak terputus.

Dibuat dengan ❤️ untuk keperluan Tugas Besar Keilmuan. 
Selamat membaca!
