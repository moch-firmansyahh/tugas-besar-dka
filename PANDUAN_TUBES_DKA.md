# Panduan Tugas Besar DKA
## Implementasi Fuzzy Logic

---

## 👥 Ketentuan Kelompok

- Tugas dikerjakan secara **berkelompok (maksimal 3 orang)**
- Setiap kelompok wajib memiliki:
  - Topik permasalahan yang **berbeda**
  - Dataset yang **berbeda**
- Topik dan dataset harus melalui **approval dosen** terlebih dahulu
- **Tidak diperbolehkan** adanya duplikasi antar kelompok di semua kelas

---

## 📊 Ketentuan Dataset

- Dataset wajib berupa **data nyata** (bukan sintetis/buatan)
- Minimal **5.000 baris data**
- Setiap baris memiliki minimal **5 variabel input** dan **1 output**
- Wajib mencantumkan **sumber dataset berupa link**

---

## 🧠 Ketentuan Fuzzy Logic

### Yang Harus Didesain

- Variabel linguistik
- Fungsi keanggotaan (membership function)
- Rule base — **minimal 15 rule**

### Yang Harus Diimplementasikan

- Fuzzy **Mamdani**
- Fuzzy **Sugeno**

### Proses yang Harus Dilakukan

| Proses | Keterangan |
|---|---|
| Fuzzifikasi | Mengubah input crisp ke derajat keanggotaan |
| Inferensi | Evaluasi rule base terhadap input fuzzy |
| Defuzzifikasi | Mengubah output fuzzy ke nilai crisp |

> ⚠️ **Dilarang menggunakan library fuzzy yang sudah jadi. Semua harus dibangun from scratch.**

---

## 📋 Analisis yang WAJIB Dilakukan

### 1. Perbandingan Mamdani vs Sugeno

Lakukan perbandingan langsung antara kedua metode pada dataset yang sama.

### 2. Evaluasi Performa

Evaluasi disesuaikan dengan jenis data yang digunakan:

| Kondisi Data | Metrik yang Digunakan |
|---|---|
| Dataset memiliki label / ground truth | Akurasi, Precision, Recall, F1-Score, atau metrik klasifikasi lainnya |
| Output berupa nilai kontinu | MAE (Mean Absolute Error) atau MSE (Mean Squared Error) |
| Tidak ada ground truth | Evaluasi kualitatif — nilai apakah output masuk akal dan konsisten dengan rule |

### 3. Interpretasi

- Kelebihan dan kekurangan **Mamdani**
- Kelebihan dan kekurangan **Sugeno**
- Kesimpulan metode mana yang lebih sesuai untuk kasus yang dikerjakan

---

## 📁 Output yang Dikumpulkan

| File | Format |
|---|---|
| Laporan | `.pdf` |
| Source code | `.ipynb` (Jupyter Notebook) |

---

## ⭐ Bonus (Opsional)

| Pengembangan Tambahan | Nilai Bonus Maksimal |
|---|---|
| Aplikasi web berbasis **Streamlit** | +5 poin |
| Integrasi **Fuzzy Logic + Machine Learning** | +10 poin |
| Integrasi **Fuzzy Logic + Deep Learning** | +20 poin |

> ⚠️ **Penting:** Machine Learning dan Deep Learning **tidak boleh menggantikan** sistem fuzzy. Keduanya hanya boleh menjadi komponen tambahan yang berjalan bersama fuzzy.

---

## 🗓️ Pengumpulan & Evaluasi

| Item | Detail |
|---|---|
| Deadline pengumpulan | **8 Juni 2026** |
| Format evaluasi | Tidak ada presentasi formal — langsung **sesi tanya jawab (Q&A)** |
| Waktu pelaksanaan Q&A | Minggu ke-15 perkuliahan |
| Durasi Q&A per kelompok | Sekitar **15 menit** |
| Kehadiran | Seluruh anggota kelompok **WAJIB hadir secara onsite/luring** |

---

## 🔗 Referensi

- List kelompok beserta dataset yang digunakan tersedia di file:
  **`LIST TUBES DKA 2526.xlsx`**

---

*Dokumen ini merupakan hasil konversi dari panduan resmi tugas besar mata kuliah Dasar Kecerdasan Artifisial (DKA).*
