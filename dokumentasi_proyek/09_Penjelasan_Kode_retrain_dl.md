# Bedah Kode Secara Mendalam: `retrain_dl_hybrid.py`

File `retrain_dl_hybrid.py` adalah skrip yang bertugas membangun "otak" Jaringan Saraf Tiruan (*Artificial Neural Networks*). Mari kita bedah fungsi blok-blok *backend* cerdas ini lapis demi lapis.

---

## 1. Import Library Keras & Scikit-Learn (Baris 14-22)
```python
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import joblib
```
- `tensorflow` & `keras`: Modul utama (Framework Google) untuk membangun lapisan arsitektur Deep Learning (*Dense, Dropout, Sequential*).
- `train_test_split`: Fungsi pemecah array dataset agar terbagi menjadi proporsi "Ujian" dan "Latihan" secara acak.
- `StandardScaler`: Formula pengecilan angka drastis (Standardisasi berbasis kurva lonceng/Z-Score).
- `joblib`: Digunakan untuk membekukan memori skrip (menyimpan object Scaler ke bentuk `.pkl`).

## 2. Bagian 1 & 2: Rekonstruksi Fuzzy & Load Dataset (Baris 24-134)
Blok awal ini adalah murni *copy-paste* dari `app.py`. Ia mendefinisikan Fungsi Keanggotaan, 42 `RULES` Baru, dan metode `mamdani_inferensi` dengan `PRODUCT t-norm`.
Setelahnya, baris ini meng- *load* dataset `cardio_train1.xlsx` menggunakan Pandas dengan fungsi Boolean filter batas medis (Sistolik 60-250, dst) serta perumusan variabel `bmi`.

## 3. Bagian 3: Komputasi Skor Hybrid Mamdani (Baris 136-150)
```python
print("\n[2/5] Computing Mamdani scores for all data...")
mamdani_scores = []
for idx, (_, row) in enumerate(df_clean.iterrows()):
    score = mamdani_inferensi(row['age'], row['ap_hi'], row['bmi'],
                               row['ap_lo'], row['cholesterol'], row['gluc'])
    mamdani_scores.append(score)
df_clean['mamdani_score'] = mamdani_scores
```
Di sinilah keajaiban **HYBRID** terjadi. Jaringan Saraf tidak murni belajar dari data telanjang (seperti Tensi). Melainkan, skrip ini memaksa setiap baris pasien melewati kalkulator Fuzzy Mamdani terlebih dahulu. Nilai persentase Fuzzy (misal: 62.4%) ditambahkan menjadi kolom baru bernama `mamdani_score`. Sehingga mesin belajar dari "Pendapat Pakar Logika" sebagai sebuah petunjuk (*Feature / Clue*). Karena menggunakan Mamdani murni (bukan sampel), iterasi perhitungan ini sengaja dirancang sangat lama (sekitar ~5 menit komputasi intensif CPU).

## 4. Bagian 4: Pemecahan dan Penskalaan (Baris 152-169)
```python
X = df_clean[FEATURE_COLS].values
y = df_clean['cardio'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```
- Array fitur (`X`) memuat 7 parameter, array kunci jawaban (`y`) memuat 0/1.
- `train_test_split(..., test_size=0.2)`: Secara acak merobek Excel, menyisihkan 20% khusus untuk tes agar model tidak curang (karena tidak pernah melihat kunci jawaban bagian tes ini). Parameter `stratify=y` memastikan rasio pasien sakit dan sehat pada pecahan tersebut seimbang.

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```
Penting! `fit_transform` menyuruh mesin membaca distribusi data *training* (Mencari rata-rata & deviasi), lalu menskalakannya. Di sisi lain, *test set* HANYA memakai perintah `transform` untuk mencegah kebocoran informasi distribusi ke dalam model.

## 5. Bagian 5: Mendirikan Gedung Arsitektur Saraf (Baris 171-199)
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(len(FEATURE_COLS),)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(32, activation='relu'),
    ...
    keras.layers.Dense(1, activation='sigmoid')
])
```
- `Sequential`: Berarti data akan mengalir dari atas ke bawah.
- `Dense(64)`: Lapis pertama berisi 64 otak mini (Neuron) yang menempel satu sama lain *Fully-Connected*.
- `Activation='relu'`: Menonaktifkan angka negatif yang merusak gradien matematika.
- `Dropout`: Melatih model lebih keras dengan secara buta menembak mati 30% memori acak setiap putaran iterasi agar tidak manja/menghafal.
- Lapis paling dasar berjenis `Dense(1)` dengan `sigmoid` bertugas memeras ratusan sinyal dari atasnya menjadi 1 angka pasti pecahan (misal `0.78`) yang berarti 78% yakin Sakit Jantung.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```
Merupakan penyatuan akhir (*Compile*) di mana *Loss Function* menggunakan standar dua target klasifikasi, serta memakai alat *Optimizer Adam* yang canggih memutakhirkan kalkulus turunan *Gradient Descent*.

```python
history = model.fit(X_train_scaled, y_train, epochs=30, batch_size=64, validation_split=0.2)
```
Skrip inti pemicu belajar. Berjalan 30 putaran (`epochs=30`), menyerap data sebanyak 64 baris sekali telan (`batch_size=64`), dan dari sisa bagian 80% Latihan itu, ia masih disiplin menyisihkan 20% lagi (`validation_split`) untuk bercermin.

## 6. Bagian 6: Ujian Kelulusan dan Penyimpanan (Baris 201-226)
```python
y_pred_prob = model.predict(X_test_scaled, verbose=0).flatten()
y_pred = (y_pred_prob >= 0.5).astype(int)
```
Data `X_test` (Ujian Nasional) yang diumpankan ke model disaring. Jika keyakinan mesin $\ge$ 50% (0.5), maka dibulatkan menjadi 1.

Setelah itu, hasil `y_pred` dibandingkan dengan `y_test` diumpankan ke pustaka *Scikit-Learn* (`classification_report` & `confusion_matrix`) yang akan di-print ke layar.
Terakhir, `model.save('model_hybrid_dka.h5')` dan `joblib.dump(scaler, 'scaler_hybrid_dka.pkl')` dipanggil. Model ini berhasil menamatkan pelatihannya dan otaknya disalin permanen ke *Hard Drive* lokal siap digunakan *Streamlit*.
