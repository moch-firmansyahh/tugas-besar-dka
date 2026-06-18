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
