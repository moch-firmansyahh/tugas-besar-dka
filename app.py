import streamlit as st
import tensorflow as tf
import joblib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import math

st.set_page_config(page_title="Fuzzy DKA - Risiko Kardiovaskular", layout="wide")

# ==========================================
# 1. MEMBERSHIP FUNCTIONS
# ==========================================

# Trapezoidal MF
def trapmf(x, a, b, c, d):
    if x <= a or x >= d: return 0.0
    if b <= x <= c:       return 1.0
    if x < b:             return (x - a) / (b - a)
    return (d - x) / (d - c)

# Triangular MF
def trimf(x, a, b, c):
    if x <= a or x >= c: return 0.0
    if x <= b:            return (x - a) / (b - a)
    return (c - x) / (c - b)

# --- USIA ---
def mu_usia_muda(x):   return trapmf(x, 20, 25, 40, 50)
def mu_usia_sedang(x): return trapmf(x, 40, 50, 55, 62)
def mu_usia_tua(x):    return trapmf(x, 55, 62, 70, 75)

# --- TEKANAN DARAH SISTOLIK (ap_hi) ---
def mu_bp_normal(x):   return trapmf(x, 60, 70, 110, 125)
def mu_bp_pre(x):      return trapmf(x, 110, 125, 135, 145)
def mu_bp_hiper(x):    return trapmf(x, 135, 145, 200, 250)

# --- TEKANAN DARAH DIASTOLIK (ap_lo) ---
def mu_bplo_normal(x): return trapmf(x, 40, 60, 80, 85)
def mu_bplo_pre(x):    return trapmf(x, 80, 85, 90, 100)
def mu_bplo_hiper(x):  return trapmf(x, 90, 100, 150, 180)

# --- BMI ---
def mu_bmi_normal(x):  return trapmf(x, 10, 15, 22, 26)
def mu_bmi_over(x):    return trapmf(x, 22, 26, 28, 32)
def mu_bmi_obese(x):   return trapmf(x, 28, 32, 55, 60)

# --- KOLESTEROL ---
def mu_chol_normal(x): return trimf(x, 0, 1, 2)
def mu_chol_tinggi(x): return trimf(x, 1, 3, 4)

# --- OUTPUT: RISIKO (Mamdani) ---
def mu_risk_rendah(s): return trapmf(s, -5, 0, 25, 45)
def mu_risk_sedang(s): return trimf(s, 30, 50, 70)
def mu_risk_tinggi(s): return trapmf(s, 55, 75, 100, 105)

# --- OUTPUT: RISIKO (Sugeno — singleton) ---
SUGENO_SINGLETON = {'rendah': 20.0, 'sedang': 50.0, 'tinggi': 85.0}

OUTPUT_MF = {
    'rendah': mu_risk_rendah,
    'sedang': mu_risk_sedang,
    'tinggi': mu_risk_tinggi,
}

# ==========================================
# 2. RULE BASE (25 Aturan)
# ==========================================
RULES = [
    # (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, konsekuen)
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

# ==========================================
# 3. FUNGSI INFERENSI
# ==========================================

def fuzzifikasi(usia, bp, bmi, ap_lo, chol):
    return {
        'usia_muda'  : mu_usia_muda(usia),
        'usia_sedang': mu_usia_sedang(usia),
        'usia_tua'   : mu_usia_tua(usia),
        'bp_normal'  : mu_bp_normal(bp),
        'bp_pre'     : mu_bp_pre(bp),
        'bp_hiper'   : mu_bp_hiper(bp),
        'bplo_normal': mu_bplo_normal(ap_lo),
        'bplo_pre'   : mu_bplo_pre(ap_lo),
        'bplo_hiper' : mu_bplo_hiper(ap_lo),
        'bmi_normal' : mu_bmi_normal(bmi),
        'bmi_over'   : mu_bmi_over(bmi),
        'bmi_obese'  : mu_bmi_obese(bmi),
        'chol_normal': mu_chol_normal(chol),
        'chol_tinggi': mu_chol_tinggi(chol),
    }

def evaluasi_rule(usia, bp, bmi, ap_lo, chol):
    result = []
    for (fn_usia, fn_bp, fn_bplo, fn_bmi, fn_chol, konsekuen) in RULES:
        alpha = min(fn_usia(usia), fn_bp(bp), fn_bplo(ap_lo), fn_bmi(bmi), fn_chol(chol))
        result.append((alpha, konsekuen))
    return result

def mamdani_inferensi(usia, bp, bmi, ap_lo, chol, n=400):
    firing = evaluasi_rule(usia, bp, bmi, ap_lo, chol)
    S_vals = np.linspace(0, 100, n)
    agg    = np.zeros(n)
    for (alpha, konsekuen) in firing:
        mf_fn = OUTPUT_MF[konsekuen]
        for i, s in enumerate(S_vals):
            agg[i] = max(agg[i], min(alpha, mf_fn(s)))
    denom  = np.sum(agg)
    output = float(np.sum(S_vals * agg) / denom) if denom > 0 else 50.0
    return output

def sugeno_inferensi(usia, bp, bmi, ap_lo, chol):
    firing = evaluasi_rule(usia, bp, bmi, ap_lo, chol)
    num = sum(a * SUGENO_SINGLETON[k] for (a, k) in firing)
    den = sum(a for (a, _) in firing)
    return float(num / den) if den > 0 else 50.0

def label_risiko(score):
    if score < 40:  return 'Rendah'
    if score < 65:  return 'Sedang'
    return 'Tinggi'

# ==========================================
# 4. VISUALISASI
# ==========================================

def plot_mamdani(usia, bp, bmi, ap_lo, chol):
    firing  = evaluasi_rule(usia, bp, bmi, ap_lo, chol)
    S_vals  = np.linspace(0, 100, 400)
    
    alpha_per = {'rendah': 0.0, 'sedang': 0.0, 'tinggi': 0.0}
    for (a, k) in firing:
        alpha_per[k] = max(alpha_per[k], a)
        
    alpha_rendah = round(alpha_per['rendah'], 3)
    alpha_sedang = round(alpha_per['sedang'], 3)
    alpha_tinggi = round(alpha_per['tinggi'], 3)
    
    y_rendah_trunc = np.array([min(alpha_rendah, mu_risk_rendah(s)) for s in S_vals])
    y_sedang_trunc = np.array([min(alpha_sedang, mu_risk_sedang(s)) for s in S_vals])
    y_tinggi_trunc = np.array([min(alpha_tinggi, mu_risk_tinggi(s)) for s in S_vals])
    
    y_agg = np.maximum(np.maximum(y_rendah_trunc, y_sedang_trunc), y_tinggi_trunc)
    
    denom   = np.sum(y_agg)
    centroid = float(np.sum(S_vals * y_agg) / denom) if denom > 0 else 50.0
    
    BG   = '#0d1117'
    CARD = '#161b22'
    fig  = plt.figure(figsize=(11, 6), facecolor=BG)
    ax   = fig.add_subplot(111, facecolor=CARD)
    
    BLUE   = '#3b82f6'
    GREEN  = '#10b981'
    AMBER  = '#f59e0b'
    LBLUE  = '#60a5fa'
    GRID   = '#21262d'
    
    ax.fill_between(S_vals, 0, y_rendah_trunc, color=BLUE,  alpha=0.25)
    ax.fill_between(S_vals, 0, y_sedang_trunc, color=GREEN, alpha=0.25)
    ax.fill_between(S_vals, 0, y_tinggi_trunc, color=AMBER, alpha=0.25)
    
    ax.plot(S_vals, y_rendah_trunc, color=BLUE,  lw=2,   label=f'Rendah  (α={alpha_rendah})')
    ax.plot(S_vals, y_sedang_trunc, color=GREEN, lw=2,   label=f'Sedang  (α={alpha_sedang})')
    ax.plot(S_vals, y_tinggi_trunc, color=AMBER, lw=2,   label=f'Tinggi  (α={alpha_tinggi})')
    ax.fill_between(S_vals, 0, y_agg, color='#1e293b', alpha=0.55, label='Aggregated Area')
    ax.plot(S_vals, y_agg, color=LBLUE, lw=2.5, linestyle='-', alpha=0.9)
    ax.axvline(x=centroid, color='#ffffff', ls=':', lw=2, label=f'Centroid ({centroid:.1f}%)')
    ax.text(centroid + 1.5, 1.02, f'{centroid:.1f}%', color='#ffffff', fontsize=10, fontweight='bold', va='bottom')
    
    ax.set_title('Mamdani — Agregasi & Defuzzifikasi', color='#ffffff', fontsize=14, fontweight='bold', pad=12, loc='left')
    ax.set_xlabel('Risk Level (%)', color='#8b949e', fontsize=11)
    ax.set_ylabel('Membership (μ)', color='#8b949e', fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.15)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.tick_params(colors='#8b949e', labelsize=10)
    ax.grid(True, color=GRID, lw=0.8)
    for spine in ax.spines.values(): spine.set_color(GRID)
    
    legend = ax.legend(loc='upper left', facecolor='#1c2028', edgecolor=GRID, labelcolor='#c9d1d9', fontsize=10)
    
    info = (f'Input  →  Usia: {usia:.1f} th | BP Sistolik: {bp} mmHg | BP Diastolik: {ap_lo} mmHg | BMI: {bmi:.1f} | Kolesterol: {chol}\n'
            f'Output →  Centroid Mamdani: {centroid:.2f}%  |  Kategori: {label_risiko(centroid)}')
    fig.text(0.5, 0.01, info, ha='center', color='#8b949e', fontsize=10, bbox=dict(fc='#161b22', ec=GRID, pad=5))
    plt.tight_layout(rect=[0, 0.07, 1, 1])
    return fig

def plot_sugeno(usia, bp, bmi, ap_lo, chol):
    firing = evaluasi_rule(usia, bp, bmi, ap_lo, chol)
    active = [(i+1, a, k) for i, (a, k) in enumerate(firing) if a > 0]
    sugeno_out = sugeno_inferensi(usia, bp, bmi, ap_lo, chol)
    
    COLOR_MAP = {'rendah': '#3b82f6', 'sedang': '#10b981', 'tinggi': '#f59e0b'}
    BG   = '#0d1117'
    CARD = '#161b22'
    GRID = '#21262d'
    
    fig = plt.figure(figsize=(13, 12), facecolor=BG)
    gs  = gridspec.GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)
    
    # Panel 1: Usia
    ax1 = fig.add_subplot(gs[0, 0], facecolor=CARD)
    u_x = np.linspace(20, 80, 500)
    ax1.plot(u_x, [mu_usia_muda(v) for v in u_x],   color='#3b82f6', lw=2, label='Muda')
    ax1.plot(u_x, [mu_usia_sedang(v) for v in u_x], color='#10b981', lw=2, label='Sedang')
    ax1.plot(u_x, [mu_usia_tua(v) for v in u_x],    color='#f59e0b', lw=2, label='Tua')
    ax1.axvline(usia, color='#ff6b6b', ls='--', lw=1.5, label=f'Input={usia:.1f}')
    ax1.set_title('Fungsi Keanggotaan (MF) Usia', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax1.set_ylabel('μ', color='#8b949e', fontsize=10)
    ax1.legend(facecolor='#1c2028', edgecolor=GRID, labelcolor='#c9d1d9', fontsize=8)
    ax1.grid(True, color=GRID, lw=0.6); _ = [s.set_color(GRID) for s in ax1.spines.values()]
    ax1.tick_params(colors='#8b949e', labelsize=8)
    
    # Panel 2: BP Sistolik
    ax2 = fig.add_subplot(gs[0, 1], facecolor=CARD)
    b_x = np.linspace(50, 260, 500)
    ax2.plot(b_x, [mu_bp_normal(v) for v in b_x], color='#3b82f6', lw=2, label='Normal')
    ax2.plot(b_x, [mu_bp_pre(v) for v in b_x],    color='#10b981', lw=2, label='Pre-Hiper')
    ax2.plot(b_x, [mu_bp_hiper(v) for v in b_x],  color='#f59e0b', lw=2, label='Hipertensi')
    ax2.axvline(bp, color='#ff6b6b', ls='--', lw=1.5, label=f'Input={bp}')
    ax2.set_title('Fungsi Keanggotaan (MF) Tekanan Sistolik', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax2.set_ylabel('μ', color='#8b949e', fontsize=10)
    ax2.legend(facecolor='#1c2028', edgecolor=GRID, labelcolor='#c9d1d9', fontsize=8)
    ax2.grid(True, color=GRID, lw=0.6); _ = [s.set_color(GRID) for s in ax2.spines.values()]
    ax2.tick_params(colors='#8b949e', labelsize=8)
    
    # Panel Tambahan: BP Diastolik & Kolesterol
    ax_bplo = fig.add_subplot(gs[1, 0], facecolor=CARD)
    bplo_x = np.linspace(30, 200, 500)
    ax_bplo.plot(bplo_x, [mu_bplo_normal(v) for v in bplo_x], color='#3b82f6', lw=2, label='Normal')
    ax_bplo.plot(bplo_x, [mu_bplo_pre(v) for v in bplo_x],    color='#10b981', lw=2, label='Pre-Hiper')
    ax_bplo.plot(bplo_x, [mu_bplo_hiper(v) for v in bplo_x],  color='#f59e0b', lw=2, label='Hipertensi')
    ax_bplo.axvline(ap_lo, color='#ff6b6b', ls='--', lw=1.5, label=f'Input={ap_lo}')
    ax_bplo.set_title('Fungsi Keanggotaan (MF) Tekanan Diastolik', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax_bplo.set_ylabel('μ', color='#8b949e', fontsize=10)
    ax_bplo.grid(True, color=GRID, lw=0.6); _ = [s.set_color(GRID) for s in ax_bplo.spines.values()]
    ax_bplo.tick_params(colors='#8b949e', labelsize=8)

    ax_chol = fig.add_subplot(gs[1, 1], facecolor=CARD)
    chol_x = np.linspace(0, 5, 100)
    ax_chol.plot(chol_x, [mu_chol_normal(v) for v in chol_x], color='#3b82f6', lw=2, label='Normal')
    ax_chol.plot(chol_x, [mu_chol_tinggi(v) for v in chol_x], color='#f59e0b', lw=2, label='Tinggi')
    ax_chol.axvline(chol, color='#ff6b6b', ls='--', lw=1.5, label=f'Input={chol}')
    ax_chol.set_title('Fungsi Keanggotaan (MF) Tingkat Kolesterol', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax_chol.set_ylabel('μ', color='#8b949e', fontsize=10)
    ax_chol.grid(True, color=GRID, lw=0.6); _ = [s.set_color(GRID) for s in ax_chol.spines.values()]
    ax_chol.tick_params(colors='#8b949e', labelsize=8)

    # Panel 3: Firing Strength
    ax3 = fig.add_subplot(gs[2, 0], facecolor=CARD)
    if active:
        rule_ids = [f'R{r}' for (r, a, k) in active]
        alphas   = [a for (r, a, k) in active]
        colors   = [COLOR_MAP[k] for (r, a, k) in active]
        bars = ax3.barh(rule_ids, alphas, color=colors, edgecolor=GRID, height=0.6)
        for bar, alpha in zip(bars, alphas):
            ax3.text(alpha + 0.01, bar.get_y() + bar.get_height()/2, f'{alpha:.3f}', va='center', color='#c9d1d9', fontsize=8)
    ax3.set_xlim(0, 1.15)
    ax3.set_title('Kekuatan Aturan Aktif (Firing Strength)', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax3.set_xlabel('Firing Strength', color='#8b949e', fontsize=9)
    patches = [mpatches.Patch(color=COLOR_MAP[k], label=k.capitalize()) for k in COLOR_MAP]
    ax3.legend(handles=patches, facecolor='#1c2028', edgecolor=GRID, labelcolor='#c9d1d9', fontsize=8, loc='lower right')
    ax3.grid(True, axis='x', color=GRID, lw=0.6)
    _ = [s.set_color(GRID) for s in ax3.spines.values()]
    ax3.tick_params(colors='#8b949e', labelsize=8)
    
    # Panel 4: Sugeno Weighted
    ax4 = fig.add_subplot(gs[2, 1], facecolor=CARD)
    if active:
        rule_ids  = [f'R{r}\n({k[:3]})' for (r, a, k) in active]
        contrib   = [a * SUGENO_SINGLETON[k] for (r, a, k) in active]
        colors    = [COLOR_MAP[k] for (r, a, k) in active]
        x_pos     = range(len(active))
        bars = ax4.bar(x_pos, contrib, color=colors, edgecolor=GRID, width=0.6, alpha=0.85)
        for bar, c in zip(bars, contrib):
            if c > 0:
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{c:.2f}', ha='center', color='#c9d1d9', fontsize=7.5)
        ax4.set_xticks(list(x_pos))
        ax4.set_xticklabels(rule_ids, fontsize=7.5, color='#8b949e')
    ax4.axhline(sugeno_out, color='#ff6b6b', ls='--', lw=2, label=f'WA = {sugeno_out:.2f}%')
    ax4.set_title('Kontribusi Prediksi Sugeno (Weighted)', color='#c9d1d9', fontsize=11, fontweight='bold')
    ax4.set_ylabel('α × z', color='#8b949e', fontsize=9)
    ax4.legend(facecolor='#1c2028', edgecolor=GRID, labelcolor='#c9d1d9', fontsize=9)
    ax4.grid(True, axis='y', color=GRID, lw=0.6)
    _ = [s.set_color(GRID) for s in ax4.spines.values()]
    ax4.tick_params(colors='#8b949e', labelsize=8)
    
    fig.suptitle(
        f'Sugeno FIS | Usia: {usia:.1f} | BP Sis: {bp} | BP Dia: {ap_lo} | BMI: {bmi:.1f} | Kolesterol: {chol}\n'
        f'Output Weighted Average: {sugeno_out:.2f}%  →  Kategori: {label_risiko(sugeno_out)}',
        color='#ffffff', fontsize=12, fontweight='bold', y=1.01
    )
    plt.tight_layout()
    return fig

# ==========================================
# 5. STREAMLIT UI
# ==========================================


@st.cache_resource
def load_model_and_scaler():
    try:
        loaded_model  = tf.keras.models.load_model('model_hybrid_dka.h5')
        loaded_scaler = joblib.load('scaler_hybrid_dka.pkl')
        return loaded_model, loaded_scaler
    except Exception as e:
        return None, None

model_dl, scaler_dl = load_model_and_scaler()

st.title("🫀 Fuzzy Inference System - Risiko Kardiovaskular")
st.markdown("""
Aplikasi web ini menggunakan **Logika Fuzzy (Mamdani & Sugeno)** untuk memprediksi risiko penyakit kardiovaskular berdasarkan 5 variabel input:
Usia, Tekanan Darah Sistolik, Tekanan Darah Diastolik, BMI, dan Kolesterol.
""")

st.sidebar.header("Data Pasien (Input)")
in_usia = st.sidebar.slider("Usia (Tahun)", 20, 80, 50)
in_aphi = st.sidebar.slider("Tekanan Darah Sistolik (mmHg)", 60, 250, 120)
in_aplo = st.sidebar.slider("Tekanan Darah Diastolik (mmHg)", 40, 150, 80)
in_bmi = st.sidebar.slider("Body Mass Index (BMI)", 10.0, 50.0, 24.5)
in_chol = st.sidebar.selectbox("Tingkat Kolesterol (1=Normal, 2=Tinggi, 3=Sangat Tinggi)", [1, 2, 3])

if st.sidebar.button("Hitung Prediksi Risiko", type="primary"):
    st.markdown("---")
    st.subheader("📊 Hasil Prediksi")
    
    score_m = mamdani_inferensi(in_usia, in_aphi, in_bmi, in_aplo, in_chol)
    score_s = sugeno_inferensi(in_usia, in_aphi, in_bmi, in_aplo, in_chol)
    
    dl_prob = 0.0
    dl_label = "Model Not Found"
    if model_dl is not None and scaler_dl is not None:
        X_input = scaler_dl.transform([[in_usia, in_aphi, in_aplo, in_bmi, in_chol, score_m]])
        dl_prob = float(model_dl.predict(X_input, verbose=0)[0][0])
        dl_label = 'Tinggi' if dl_prob >= 0.5 else 'Rendah'
        
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Skor Mamdani", value=f"{score_m:.2f}%", delta=label_risiko(score_m), delta_color="inverse")
    with col2:
        st.metric(label="Skor Sugeno", value=f"{score_s:.2f}%", delta=label_risiko(score_s), delta_color="inverse")
    with col3:
        if model_dl is not None:
            st.metric(label="DL Hybrid", value=f"{dl_prob*100:.2f}%", delta=dl_label, delta_color="inverse")
        else:
            st.metric(label="DL Hybrid", value="N/A", delta="File Model Hilang")
        
    st.markdown("---")
    st.subheader("📈 Visualisasi Proses Fuzzy (Mamdani)")
    fig_m = plot_mamdani(in_usia, in_aphi, in_bmi, in_aplo, in_chol)
    st.pyplot(fig_m)
    
    st.markdown("---")
    st.subheader("📈 Visualisasi Proses Fuzzy (Sugeno)")
    fig_s = plot_sugeno(in_usia, in_aphi, in_bmi, in_aplo, in_chol)
    st.pyplot(fig_s)
    
    st.success("Perhitungan berhasil diselesaikan!")
