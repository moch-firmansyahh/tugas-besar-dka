"""
=============================================================
Evaluasi Performa Fuzzy Inference System (Sebelum vs Sesudah)
=============================================================
Script ini menghitung dan membandingkan metrik akurasi:
- SEBELUM: 5 input, 25 rules, MIN t-norm, Singleton(20,50,85), threshold 55%
- SESUDAH: 6 input, 42 rules, PRODUCT t-norm, Singleton(15,45,85), threshold 50%

Metrik: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
Bisa di-copy paste ke dalam Jupyter Notebook.
"""
import pandas as pd
import numpy as np
from collections import Counter

# ==========================================
# LOAD & CLEAN DATA
# ==========================================
print("Loading dataset...")
df = pd.read_excel('cardio_train1.xlsx')
df_clean = df[(df['ap_hi'] >= 60) & (df['ap_hi'] <= 250) &
              (df['ap_lo'] >= 40) & (df['ap_lo'] <= 150)].copy()
df_clean['bmi'] = df_clean['weight'] / (df_clean['height']/100)**2
print(f"Dataset: {len(df_clean)} samples (after cleaning)")
print(f"Cardio distribution: {dict(Counter(df_clean['cardio']))}")

# ==========================================
# MEMBERSHIP FUNCTIONS (same for both versions)
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

# Input MFs
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

# Output MFs (Mamdani)
def mu_risk_rendah(s): return trapmf(s, -5, 0, 25, 45)
def mu_risk_sedang(s): return trimf(s, 30, 50, 70)
def mu_risk_tinggi(s): return trapmf(s, 55, 75, 100, 105)

# ==========================================
# VERSION LAMA (SEBELUM) — 5 input, 25 rules, MIN, Singleton(20,50,85)
# ==========================================
RULES_OLD = [
    (mu_usia_muda,   mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, 'rendah'),
    (mu_usia_muda,   mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_normal, 'rendah'),
    (mu_usia_muda,   mu_bp_normal, mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, 'sedang'),
    (mu_usia_muda,   mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, 'rendah'),
    (mu_usia_muda,   mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, 'sedang'),
    (mu_usia_muda,   mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, 'tinggi'),
    (mu_usia_muda,   mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_tinggi, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, 'rendah'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_pre,    mu_bmi_obese,  mu_chol_tinggi, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, 'sedang'),
    (mu_usia_sedang, mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, 'tinggi'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, 'tinggi'),
    (mu_usia_sedang, mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_normal, 'sedang'),
    (mu_usia_tua,    mu_bp_normal, mu_bplo_normal, mu_bmi_normal, mu_chol_normal, 'sedang'),
    (mu_usia_tua,    mu_bp_normal, mu_bplo_normal, mu_bmi_over,   mu_chol_tinggi, 'tinggi'),
    (mu_usia_tua,    mu_bp_pre,    mu_bplo_pre,    mu_bmi_normal, mu_chol_normal, 'sedang'),
    (mu_usia_tua,    mu_bp_pre,    mu_bplo_pre,    mu_bmi_over,   mu_chol_tinggi, 'tinggi'),
    (mu_usia_tua,    mu_bp_pre,    mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, 'tinggi'),
    (mu_usia_tua,    mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_normal, mu_chol_normal, 'tinggi'),
    (mu_usia_tua,    mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_over,   mu_chol_tinggi, 'tinggi'),
    (mu_usia_tua,    mu_bp_hiper,  mu_bplo_hiper,  mu_bmi_obese,  mu_chol_tinggi, 'tinggi'),
    (mu_usia_muda,   mu_bp_normal, mu_bplo_hiper,  mu_bmi_normal, mu_chol_tinggi, 'sedang'),
    (mu_usia_sedang, mu_bp_normal, mu_bplo_hiper,  mu_bmi_over,   mu_chol_tinggi, 'tinggi'),
    (mu_usia_tua,    mu_bp_hiper,  mu_bplo_normal, mu_bmi_obese,  mu_chol_normal, 'tinggi'),
]

SINGLETON_OLD = {'rendah': 20.0, 'sedang': 50.0, 'tinggi': 85.0}

# ==========================================
# VERSION BARU (SESUDAH) — 6 input, 42 rules, PRODUCT, Singleton(15,45,85)
# ==========================================
RULES_NEW = [
    # MUDA (12)
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
    # SEDANG (15)
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
    # TUA (15)
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

SINGLETON_NEW = {'rendah': 15.0, 'sedang': 45.0, 'tinggi': 85.0}

# ==========================================
# INFERENCE FUNCTIONS
# ==========================================

def sugeno_old(row):
    """Versi lama: 5 input, MIN t-norm"""
    firing = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, konsekuen) in RULES_OLD:
        alpha = min(fn_usia(row['age']), fn_bp(row['ap_hi']),
                    fn_bplo(row['ap_lo']), fn_bmi(row['bmi']),
                    fn_chol(row['cholesterol']))
        firing.append((alpha, konsekuen))
    num = sum(a * SINGLETON_OLD[k] for (a, k) in firing)
    den = sum(a for (a, _) in firing)
    return float(num / den) if den > 0 else 50.0

def sugeno_new(row):
    """Versi baru: 6 input, PRODUCT t-norm"""
    firing = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, fn_gluc, konsekuen) in RULES_NEW:
        alpha = (fn_usia(row['age']) * fn_bp(row['ap_hi']) *
                 fn_bplo(row['ap_lo']) * fn_bmi(row['bmi']) *
                 fn_chol(row['cholesterol']) * fn_gluc(row['gluc']))
        firing.append((alpha, konsekuen))
    num = sum(a * SINGLETON_NEW[k] for (a, k) in firing)
    den = sum(a for (a, _) in firing)
    return float(num / den) if den > 0 else 50.0

def mamdani_old(row, n=200):
    """Mamdani versi lama: 5 input, MIN t-norm"""
    firing = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, konsekuen) in RULES_OLD:
        alpha = min(fn_usia(row['age']), fn_bp(row['ap_hi']),
                    fn_bplo(row['ap_lo']), fn_bmi(row['bmi']),
                    fn_chol(row['cholesterol']))
        firing.append((alpha, konsekuen))
    S_vals = np.linspace(0, 100, n)
    agg = np.zeros(n)
    OUTPUT_MF_MAP = {'rendah': mu_risk_rendah, 'sedang': mu_risk_sedang, 'tinggi': mu_risk_tinggi}
    for (alpha, konsekuen) in firing:
        mf_fn = OUTPUT_MF_MAP[konsekuen]
        for i, s in enumerate(S_vals):
            agg[i] = max(agg[i], min(alpha, mf_fn(s)))
    denom = np.sum(agg)
    return float(np.sum(S_vals * agg) / denom) if denom > 0 else 50.0

def mamdani_new(row, n=200):
    """Mamdani versi baru: 6 input, PRODUCT t-norm"""
    firing = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, fn_gluc, konsekuen) in RULES_NEW:
        alpha = (fn_usia(row['age']) * fn_bp(row['ap_hi']) *
                 fn_bplo(row['ap_lo']) * fn_bmi(row['bmi']) *
                 fn_chol(row['cholesterol']) * fn_gluc(row['gluc']))
        firing.append((alpha, konsekuen))
    S_vals = np.linspace(0, 100, n)
    agg = np.zeros(n)
    OUTPUT_MF_MAP = {'rendah': mu_risk_rendah, 'sedang': mu_risk_sedang, 'tinggi': mu_risk_tinggi}
    for (alpha, konsekuen) in firing:
        mf_fn = OUTPUT_MF_MAP[konsekuen]
        for i, s in enumerate(S_vals):
            agg[i] = max(agg[i], min(alpha, mf_fn(s)))
    denom = np.sum(agg)
    return float(np.sum(S_vals * agg) / denom) if denom > 0 else 50.0

# ==========================================
# EVALUATION METRICS
# ==========================================

def compute_metrics(y_true, y_pred):
    tp = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 1)
    tn = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 0)
    fp = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 1)
    fn = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 0)
    
    accuracy  = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1        = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn
    }

# ==========================================
# RUN EVALUATION
# ==========================================
print("\n" + "=" * 70)
print("EVALUASI PERFORMA FUZZY (SEBELUM vs SESUDAH)")
print("=" * 70)

y_true = df_clean['cardio'].values.tolist()

# --- SUGENO ---
print("\n--- Menghitung Sugeno (Versi Lama)... ---")
scores_sugeno_old = [sugeno_old(row) for _, row in df_clean.iterrows()]
print("--- Menghitung Sugeno (Versi Baru)... ---")
scores_sugeno_new = [sugeno_new(row) for _, row in df_clean.iterrows()]

# --- MAMDANI (sample 5000 for speed) ---
sample_size = 5000
df_sample = df_clean.sample(n=sample_size, random_state=42)
y_true_sample = df_sample['cardio'].values.tolist()

print(f"--- Menghitung Mamdani Lama (sample {sample_size})... ---")
scores_mamdani_old = [mamdani_old(row) for _, row in df_sample.iterrows()]
print(f"--- Menghitung Mamdani Baru (sample {sample_size})... ---")
scores_mamdani_new = [mamdani_new(row) for _, row in df_sample.iterrows()]

# --- THRESHOLDS ---
configs = [
    ("Sugeno LAMA (5 input, MIN, S:20/50/85, T=55%)",    scores_sugeno_old, y_true,        55),
    ("Sugeno LAMA (5 input, MIN, S:20/50/85, T=50%)",    scores_sugeno_old, y_true,        50),
    ("Sugeno BARU (6 input, PROD, S:15/45/85, T=50%)",   scores_sugeno_new, y_true,        50),
    (f"Mamdani LAMA (5 input, MIN, T=55%, n={sample_size})", scores_mamdani_old, y_true_sample, 55),
    (f"Mamdani LAMA (5 input, MIN, T=50%, n={sample_size})", scores_mamdani_old, y_true_sample, 50),
    (f"Mamdani BARU (6 input, PROD, T=50%, n={sample_size})", scores_mamdani_new, y_true_sample, 50),
]

for name, scores, y_t, threshold in configs:
    preds = [1 if s >= threshold else 0 for s in scores]
    m = compute_metrics(y_t, preds)
    print(f"\n{'=' * 60}")
    print(f"  {name}")
    print(f"{'=' * 60}")
    print(f"  Accuracy:  {m['accuracy']*100:.2f}%")
    print(f"  Precision: {m['precision']*100:.2f}%")
    print(f"  Recall:    {m['recall']*100:.2f}%")
    print(f"  F1-Score:  {m['f1']*100:.2f}%")
    print(f"\n  Confusion Matrix:")
    print(f"                Predicted")
    print(f"                Neg     Pos")
    print(f"  Actual Neg   {m['tn']:>5}   {m['fp']:>5}")
    print(f"  Actual Pos   {m['fn']:>5}   {m['tp']:>5}")

print("\n" + "=" * 70)
print("SELESAI!")
print("=" * 70)
