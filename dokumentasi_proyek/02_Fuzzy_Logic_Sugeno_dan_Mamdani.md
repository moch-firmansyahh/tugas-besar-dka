# Logika Fuzzy: Mamdani dan Sugeno secara Mendalam

Sistem inferensi fuzzy (Fuzzy Inference System - FIS) digunakan dalam proyek ini untuk mentranslasikan pengetahuan pakar medis mengenai faktor risiko jantung ke dalam bentuk logika komputasi. Tidak seperti logika Boolean atau biner (0 atau 1), logika fuzzy mengizinkan nilai derajat kebenaran parsial di antara 0.0 (sangat salah) dan 1.0 (sangat benar).

## 1. Fuzzifikasi dan Fungsi Keanggotaan (Membership Function)
Langkah pertama dalam sistem fuzzy adalah Fuzzifikasi. Pada tahap ini, masukan tegas (crisp input) seperti tekanan darah 130 mmHg diubah menjadi **derajat keanggotaan (membership degree - μ)**.

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
