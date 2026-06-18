# Evolusi dan Peningkatan Model (Versi Lama vs Versi Baru)

Proyek ini tidak hanya sekadar membuat satu model lalu selesai, melainkan melalui proses **Peningkatan Terukur (Iterative Improvement)**. Jika Anda membuka skrip `evaluate_accuracy.py`, Anda akan melihat perbandingan antara dua versi model Fuzzy Inference System: **Versi Lama (Sebelum)** dan **Versi Baru (Sesudah)**.

Penambahan dan penyempurnaan fitur ini adalah kunci utama mengapa model yang sekarang jauh lebih kuat dan akurat. Berikut adalah rincian lengkap peningkatan yang telah dilakukan:

---

## 1. Penambahan Fitur Input (Dari 5 Menjadi 6 Variabel)
- **Versi Lama**: Hanya menggunakan 5 variabel input (Usia, Tekanan Darah Sistolik, Tekanan Darah Diastolik, BMI, dan Kolesterol).
- **Versi Baru**: Menambahkan 1 variabel krusial, yaitu **Glukosa (Gula Darah)**.
- **Alasan Peningkatan**: Secara medis, kadar gula darah tinggi (hiperglikemia/diabetes) memiliki korelasi langsung dan sangat kuat dengan kerusakan pembuluh darah. Dengan memasukkan Glukosa, model memiliki "mata ekstra" untuk menangkap pasien berisiko yang mungkin memiliki kolesterol normal namun menderita diabetes.

## 2. Ekspansi Basis Aturan / Rule Base (Dari 25 Menjadi 42 Aturan)
- **Versi Lama**: Hanya mendefinisikan 25 aturan pakar. Beberapa kombinasi kondisi yang mungkin terjadi di dunia nyata tidak ter-cover oleh sistem, sehingga menghasilkan kesimpulan yang "menggantung" atau default ke 50%.
- **Versi Baru**: Aturan diperluas menjadi **42 aturan komprehensif**.
- **Alasan Peningkatan**: Dengan bertambahnya variabel Glukosa, jumlah kemungkinan kombinasi logis (*State Space*) membesar drastis. Penambahan menjadi 42 aturan memastikan hampir semua skenario klinis profil pasien memiliki pemetaan risiko yang pasti, mulai dari pasien muda obesitas hingga pasien tua hipertensi.

## 3. Perubahan Operator T-Norm (Dari MIN menjadi PRODUCT)
- **Versi Lama**: Menggunakan operator **MIN t-norm** (Mencari nilai minimum dari sekumpulan derajat keanggotaan).
  - *Kelemahan*: Jika ada satu saja parameter yang kebetulan memiliki nilai keanggotaan sangat kecil (misal 0.1), maka keseluruhan kekuatan aturan akan langsung jatuh ke 0.1, mengabaikan parameter lain yang mungkin bernilai 0.9 (Sangat kuat).
- **Versi Baru**: Menggunakan operator **PRODUCT t-norm** (Mengalikan seluruh nilai derajat keanggotaan).
  - *Keunggulan*: Jauh lebih sensitif, halus (*smooth*), dan setiap parameter tetap memberikan kontribusi perhitungan matematis tanpa ada yang diabaikan secara paksa.

## 4. Optimasi Nilai Singleton Sugeno
- **Versi Lama**: Menggunakan konstanta baku yang kaku: `Risiko Rendah: 20.0`, `Risiko Sedang: 50.0`, `Risiko Tinggi: 85.0`.
- **Versi Baru**: Dioptimasi berdasarkan distribusi data sesungguhnya menjadi: `Risiko Rendah: 15.0`, `Risiko Sedang: 45.0`, `Risiko Tinggi: 85.0`.
- **Alasan Peningkatan**: Menurunkan titik "Rendah" dari 20 ke 15, dan "Sedang" dari 50 ke 45 membantu memberikan batas (margin) yang lebih tegas antara pasien yang benar-benar sehat dengan yang sakit, mengurangi kebingungan model di area abu-abu.

## 5. Penyesuaian Ambang Batas (Threshold) (Dari 55% ke 50%)
- **Versi Lama**: Menggunakan ambang batas kaku `55%` untuk memvonis pasien berisiko tinggi. Hal ini menyebabkan banyak penderita kardiovaskular tahap awal (skor 51-54%) lolos dari deteksi karena tidak menembus batas 55% (Angka *False Negative* tinggi).
- **Versi Baru**: Ambang batas diturunkan dan dinormalkan ke nilai tengah yang adil, yaitu `50%`. 
- **Dampak**: Sensitivitas (Recall) model dalam menemukan pasien yang benar-benar sakit naik secara signifikan, membuat aplikasi ini lebih aman dan etis untuk digunakan sebagai skrining awal medis.

---

Dengan kelima perubahan mendasar di atas, evaluasi pada skrip `evaluate_accuracy.py` menunjukkan bahwa **Versi Baru memberikan keseimbangan F1-Score dan Recall yang jauh lebih optimal** dibandingkan versi lama, sekaligus membuktikan bahwa sistem berbasis logika murni masih bisa "di-tuning" selayaknya algoritma Machine Learning!
