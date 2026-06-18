# Penjelasan Antarmuka Web (Streamlit App) Secara Komprehensif

Dalam pengembangan sistem berbasis data/AI, logika *backend* semata (Python scripts) kurang intuitif bagi End-User seperti dokter atau tenaga medis. Oleh karena itu, antarmuka pengguna grafis (GUI) interaktif dibangun menggunakan teknologi web framework bernama **Streamlit**, yang seluruh kodenya berada di dalam file `app.py`.

## 1. Apa itu Framework Streamlit?
Streamlit adalah framework *open-source* berbasis bahasa Python (dirilis tahun 2019) yang didesain secara spesifik untuk tim Machine Learning dan Data Science. Berbeda dengan framework raksasa klasik seperti Django atau Flask yang mengharuskan pengembang menulis kode perutean (routing), desain HTML, pengelolaan tata letak CSS, hingga *Javascript asynchronous AJAX* secara mandiri, Streamlit mengubah logika skrip Python biasa menjadi aplikasi Web *Single-Page Application (SPA)* dinamis hanya dalam beberapa baris perintah antarmuka. 

Setiap kali *user* (pengguna) mengubah nilai parameter pada layar antarmuka (misalnya menggeser *slider* Usia), Streamlit secara otomatis mendeteksi perubahan state (*re-run*) dan mengeksekusi ulang file Python dari atas ke bawah.

---

## 2. Bedah Struktur Kode `app.py`

Struktur `app.py` proyek ini dibagi menjadi 5 komponen utama, yang sangat tertata sesuai arsitektur *Model-View-Controller (MVC)* fungsional.

### A. Komponen "Knowledge" / Fungsi Keanggotaan (Baris 20 - 77)
Bagian paling mendasar berisi representasi komputasi matematis dari Fungsi Keanggotaan Trapesium (`trapmf`) dan Segitiga (`trimf`). 
Pada bagian ini juga terdapat representasi Output yang membedakan Mamdani dan Sugeno:
- Mamdani menggunakan kembalian fungsi kurva: `OUTPUT_MF`.
- Sugeno menggunakan deklarasi konstanta/konfigurasi Singleton dictionary: `SUGENO_SINGLETON = {'rendah': 15.0, ...}`.

### B. Komponen "Rule Base" / Basis Aturan (Baris 79 - 131)
Berisi list array Python `RULES` yang menyimpan 42 *tuple*. Setiap *tuple* ini merepresentasikan Aturan Ahli (`IF Usia ... AND BP ... THEN Risiko ...`). Disimpan sebagai referensi fungsi secara murni (*Function Pointers*), yang siap dieksekusi secara iteratif tanpa harus menggunakan rantai `if-else` bertingkat yang rawan bug.

### C. Komponen "Mesin Inferensi" / Inference Engine (Baris 133 - 188)
Ini adalah "otak prosesor" sistem pakar.
- **`evaluasi_rule`**: Looping dari 42 list `RULES`. Mengalikan skor tiap parameter (PRODUCT t-norm). Mengembalikan List berisi kumpulan kekuatan aturan (`alpha`) dan jenis label keluaran.
- **`mamdani_inferensi`**: Mengambil nilai *alpha*, memotong (*clipping*) fungsi output menggunakan metode agregasi `max-min`. Lalu melakukan kalkulasi integral area matematika linier yang dipecah dalam skala grid ukuran grid resolusi 400 (`n=400`) menggunakan array Numpy, dilanjutkan formula "Center of Mass".
- **`sugeno_inferensi`**: Melakukan perhitungan jauh lebih hemat yaitu *Weighted Average* (Bobot alpha $\times$ Singleton). Mengembalikan hasil jauh lebih instan.

### D. Komponen "Visualisasi" Matplotlib (Baris 190 - 391)
Berkat *library* Visualisasi **Matplotlib**, aplikasi Streamlit tidak hanya memberi teks jawaban "Risiko 60%".
- **`plot_mamdani`**: Men-generate figur kanvas raksasa berisi tumpang tindih kurva Trapesium dan agregasi area Mamdani yang ditandai garis putus-putus sebagai letak pasti dari titik Centroid Defuzzifikasi.
- **`plot_sugeno`**: Men-generate figur kompleks menggunakan fitur *GridSpec Matplotlib*. Memetakan 4 panel Fungsi Keanggotaan dari titik nilai input (Input vs Fungsi), diagram bar Chart horizontal untuk membuktikan Firing Strength ($\alpha$), dan bar Chart Vertikal kontribusi Sugeno secara proporsional.

### E. Komponen "Frontend Streamlit" / Tampilan Web (Baris 393 - akhir)

Bagian ini yang langsung terpapar pada pengguna secara visual dan fungsional.

**1. Sistem Caching & Load Deep Learning:**
```python
@st.cache_resource
def load_model_and_scaler():
```
Kode ini menggunakan **Decorator Caching Memory** bawaan Streamlit `@st.cache_resource`. Saat aplikasi dinyalakan, Streamlit memuat file `model_hybrid_dka.h5` yang cukup berat (Jaringan Saraf TensorFlow) beserta file *Scaler*. Hasilnya "dibekukan" di RAM. Tanpa fitur cerdas *Cache* ini, aplikasi akan menjadi lambat dan berat karena web browser akan memaksa CPU memuat ulang model yang sama persis ribuan kali ketika *user* sekadar menggerakkan satu slider Usia.

**2. Form Input Sidebar:**
Sidebar adalah area kontrol di pinggir kiri layar menggunakan perintah `st.sidebar`. Menggunakan widget modern seperti:
- `st.sidebar.number_input()`: Mengunci validasi data input agar tidak error. Misalnya Usia dibatasi dari minimal 20 sampai masimal 80. Membantu menghindari *Crash Runtime*.
- `st.sidebar.selectbox()`: Dropdown aman spesifik untuk nilai 1, 2, atau 3 (Kolesterol & Glukosa).

**3. Tombol Trigger Utama:**
```python
if st.sidebar.button("Hitung Prediksi Risiko", type="primary"):
```
Sistem dijamin tidak akan bekerja/kalkulasi sebelum *user* merasa puas dan mengklik (submit) menekan tombol berwarna primer mencolok ini. Fitur ini sangat penting agar CPU dan daya listrik tidak terbuang sia-sia akibat aplikasi menghitung otomatis saat pengguna masih salah mengetik angka.

**4. Panel Hasil & Matrix Kolom:**
```python
col1, col2, col3 = st.columns(3)
```
Membagi panel antarmuka ke dalam 3 kisi responsif sejajar menggunakan `st.columns`, setiap kolom disuntikkan widget `st.metric()` yang sangat modern mirip *Dashboard Data Analytics* untuk menampilkan hasil 3 perbandingan skor sekaligus secara cantik (Mamdani, Sugeno, dan Deep Learning Hybrid). Dilengkapi penanda panah atas/bawah secara adaptif dengan fitur `delta_color="inverse"`.

Akhirnya, kode secara asinkron (paralel) mengeksekusi kedua *builder* visual plot (`fig_m` dan `fig_s`), yang digambar ke Web Browser menggunakan perintah perender Matplotlib ke Streamlit yakni `st.pyplot()`.

---
## Cara Instalasi & Menjalankan Aplikasi
1. Pastikan ter-install bahasa pemrograman Python (Versi > 3.9).
2. Instal pustaka paket PIP yang dibutuhkan (Keras, Matplotlib, Joblib, Sklearn, Streamlit).
   `pip install pandas numpy scikit-learn tensorflow matplotlib streamlit joblib openpyxl`
3. Arahkan *Terminal/Command Prompt* PC ke dalam direktori/folder *Code tubes*.
4. Eksekusi server web Python ringan bawaan Streamlit:
   ```bash
   streamlit run app.py
   ```
5. Buka Browser (Chrome / Edge / Firefox) dan salin URL jaringan lokal `http://localhost:8501`.
