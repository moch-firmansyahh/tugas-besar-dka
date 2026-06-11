"""
=============================================================
Re-Training Model Deep Learning Hybrid (Fuzzy + DL)
=============================================================
Script ini melatih ulang model Deep Learning dengan fitur baru:
- Input: age, ap_hi, ap_lo, bmi, cholesterol, gluc, mamdani_score (7 fitur)
- Output: cardio (0/1)

Menggunakan arsitektur yang sama dengan versi sebelumnya,
ditambah fitur Glukosa dan skor Mamdani yang sudah dioptimasi.

Bisa di-copy paste ke dalam Jupyter Notebook.
"""
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# ==========================================
# 1. MEMBERSHIP FUNCTIONS & RULES (BARU)
# ==========================================
def trapmf(x, a, b, c, d):
    if x <= a or x >= d: return 0.0
    if b <= x <= c:       return 1.0
    if x < b:             return (x - a) / (b - a)
    return (d - x) / (d - c)

def trimf(x, a, b, c):
    if x <= a or x >= c: return 0.0
    if x <= b:            return (x - a) / (b - a)
    return (c - x) / (c - b)

def mu_usia_muda(x):   return trapmf(x, 20, 25, 40, 50)
def mu_usia_sedang(x): return trapmf(x, 40, 50, 55, 62)
def mu_usia_tua(x):    return trapmf(x, 55, 62, 70, 75)
def mu_bp_normal(x):   return trapmf(x, 60, 70, 110, 125)
def mu_bp_pre(x):      return trapmf(x, 110, 125, 135, 145)
def mu_bp_hiper(x):    return trapmf(x, 135, 145, 200, 250)
def mu_bplo_normal(x): return trapmf(x, 40, 60, 80, 85)
def mu_bplo_pre(x):    return trapmf(x, 80, 85, 90, 100)
def mu_bplo_hiper(x):  return trapmf(x, 90, 100, 150, 180)
def mu_bmi_normal(x):  return trapmf(x, 10, 15, 22, 26)
def mu_bmi_over(x):    return trapmf(x, 22, 26, 28, 32)
def mu_bmi_obese(x):   return trapmf(x, 28, 32, 55, 60)
def mu_chol_normal(x): return trimf(x, 0, 1, 2)
def mu_chol_tinggi(x): return trimf(x, 1, 3, 4)
def mu_gluc_normal(x): return trimf(x, 0, 1, 2)
def mu_gluc_tinggi(x): return trimf(x, 1, 2, 4)

def mu_risk_rendah(s): return trapmf(s, -5, 0, 25, 45)
def mu_risk_sedang(s): return trimf(s, 30, 50, 70)
def mu_risk_tinggi(s): return trapmf(s, 55, 75, 100, 105)

OUTPUT_MF = {'rendah': mu_risk_rendah, 'sedang': mu_risk_sedang, 'tinggi': mu_risk_tinggi}

RULES = [
    (mu_usia_muda, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'rendah'),
    (mu_usia_muda, mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'rendah'),
    (mu_usia_muda, mu_bp_normal, mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'rendah'),
    (mu_usia_muda, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_muda, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_muda, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_tinggi, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_normal, mu_bplo_hiper,  mu_bmi_normal, mu_chol_tinggi, mu_gluc_normal, 'sedang'),
    (mu_usia_muda, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_tinggi, mu_gluc_tinggi, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'rendah'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_pre,    mu_bmi_obese,  mu_chol_tinggi, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_hiper,  mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_tinggi, mu_gluc_tinggi, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_normal, mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_pre,    mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'sedang'),
    (mu_usia_tua, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_pre,    mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_tua, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_over,   mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_tua, mu_bp_hiper,  mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_tinggi, mu_gluc_tinggi, 'tinggi'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_normal, mu_bplo_pre,    mu_bmi_over,   mu_chol_normal, mu_gluc_normal, 'tinggi'),
    (mu_usia_tua, mu_bp_pre,    mu_bplo_normal, mu_bmi_normal, mu_chol_tinggi, mu_gluc_normal, 'tinggi'),
]

def mamdani_inferensi(usia, bp, bmi, ap_lo, chol, gluc, n=200):
    """Mamdani dengan PRODUCT t-norm"""
    firing = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, fn_gluc, konsekuen) in RULES:
        alpha = (fn_usia(usia) * fn_bp(bp) * fn_bplo(ap_lo) *
                 fn_bmi(bmi) * fn_chol(chol) * fn_gluc(gluc))
        firing.append((alpha, konsekuen))
    S_vals = np.linspace(0, 100, n)
    agg = np.zeros(n)
    for (alpha, konsekuen) in firing:
        mf_fn = OUTPUT_MF[konsekuen]
        for i, s in enumerate(S_vals):
            agg[i] = max(agg[i], min(alpha, mf_fn(s)))
    denom = np.sum(agg)
    return float(np.sum(S_vals * agg) / denom) if denom > 0 else 50.0

# ==========================================
# 2. LOAD & PREPARE DATA
# ==========================================
print("=" * 60)
print("  Re-Training Model Deep Learning Hybrid")
print("=" * 60)

print("\n[1/5] Loading dataset...")
df = pd.read_excel('cardio_train1.xlsx')
df_clean = df[(df['ap_hi'] >= 60) & (df['ap_hi'] <= 250) &
              (df['ap_lo'] >= 40) & (df['ap_lo'] <= 150)].copy()
df_clean['bmi'] = df_clean['weight'] / (df_clean['height'] / 100) ** 2
print(f"  Loaded {len(df_clean)} samples")

# ==========================================
# 3. COMPUTE MAMDANI SCORES FOR ALL DATA
# ==========================================
print("\n[2/5] Computing Mamdani scores for all data (this takes ~5 min)...")
mamdani_scores = []
total = len(df_clean)
for idx, (_, row) in enumerate(df_clean.iterrows()):
    score = mamdani_inferensi(row['age'], row['ap_hi'], row['bmi'],
                               row['ap_lo'], row['cholesterol'], row['gluc'])
    mamdani_scores.append(score)
    if (idx + 1) % 10000 == 0:
        print(f"  Processed {idx+1}/{total} ({(idx+1)/total*100:.0f}%)")

df_clean['mamdani_score'] = mamdani_scores
print(f"  Done! Mamdani score stats: mean={np.mean(mamdani_scores):.2f}, std={np.std(mamdani_scores):.2f}")

# ==========================================
# 4. PREPARE FEATURES & TRAIN/TEST SPLIT
# ==========================================
print("\n[3/5] Preparing features...")

# 7 fitur: age, ap_hi, ap_lo, bmi, cholesterol, gluc, mamdani_score
FEATURE_COLS = ['age', 'ap_hi', 'ap_lo', 'bmi', 'cholesterol', 'gluc', 'mamdani_score']
X = df_clean[FEATURE_COLS].values
y = df_clean['cardio'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print(f"  Train: {len(X_train)} | Test: {len(X_test)}")
print(f"  Features: {FEATURE_COLS}")

# ==========================================
# 5. BUILD & TRAIN MODEL
# ==========================================
print("\n[4/5] Training Deep Learning model...")

model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(len(FEATURE_COLS),)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

history = model.fit(
    X_train_scaled, y_train,
    epochs=30,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)

# ==========================================
# 6. EVALUATE & SAVE
# ==========================================
print("\n[5/5] Evaluating & saving model...")

# Evaluate
y_pred_prob = model.predict(X_test_scaled, verbose=0).flatten()
y_pred = (y_pred_prob >= 0.5).astype(int)

print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred, target_names=['Sehat (0)', 'Kardio (1)']))

print("--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
print(f"  TN={cm[0][0]:>5} | FP={cm[0][1]:>5}")
print(f"  FN={cm[1][0]:>5} | TP={cm[1][1]:>5}")

test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\n  Test Loss:     {test_loss:.4f}")
print(f"  Test Accuracy: {test_acc*100:.2f}%")

# Save model & scaler
model.save('model_hybrid_dka.h5')
joblib.dump(scaler, 'scaler_hybrid_dka.pkl')
print("\n  Model saved to: model_hybrid_dka.h5")
print("  Scaler saved to: scaler_hybrid_dka.pkl")

print("\n" + "=" * 60)
print("  SELESAI! Model DL Hybrid berhasil di-retrain.")
print("=" * 60)
