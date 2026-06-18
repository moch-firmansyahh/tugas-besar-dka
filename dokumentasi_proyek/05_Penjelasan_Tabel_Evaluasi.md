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
