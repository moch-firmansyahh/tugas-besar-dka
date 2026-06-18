# Panduan Sukses Presentasi Tugas Besar (Cheat Sheet)

Melihat dari kelengkapan dokumentasi yang telah kita susun (9 dokumen), proyek Anda saat ini sudah berada di standar **Tugas Akhir / Skripsi**, bukan lagi sekadar Tugas Besar biasa. 

Untuk memastikan Anda 100% siap saat didemo/dipresentasikan di depan Dosen atau Asisten Laboratorium, berikut adalah panduan urutan presentasi dan "kisi-kisi" pertanyaan yang paling sering ditanyakan, beserta jawaban pamungkasnya!

---

## 🚀 Skenario Urutan Presentasi yang Ideal

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

## 🎯 Kisi-Kisi Pertanyaan Dosen & Cara Menjawabnya

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
Berbekal pemahaman dari 9 Dokumen Markdown sebelumnya dan *Cheat Sheet* ini, nilai A sudah pasti di tangan Anda! Selamat berjuang! 🏆
