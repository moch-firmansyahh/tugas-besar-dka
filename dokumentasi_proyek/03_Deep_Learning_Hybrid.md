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
