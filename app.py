import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patheffects as pe
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════
# HELPERS & FORMATTERS (Indonesian Standard - JT, M, RB)
# ═══════════════════════════════════════════════════════════════

def format_idr_chart(x, pos=None):
    if abs(x) >= 1e9:  return f'Rp{x/1e9:.1f}M' # Miliar
    if abs(x) >= 1e6:  return f'Rp{x/1e6:.1f}JT' # Juta
    if abs(x) >= 1e3:  return f'Rp{x/1e3:.0f}RB' # Ribu
    return f'Rp{x:,.0f}'.replace(",", "X").replace(".", ",").replace("X", ".")

def format_angka_indo(x, pos=None):
    if abs(x) >= 1e9:  return f'{x/1e9:.1f}M'
    if abs(x) >= 1e6:  return f'{x/1e6:.1f}JT'
    if abs(x) >= 1e3:  return f'{x/1e3:.0f}RB'
    return f'{x:,.0f}'

def fmt_idr_kpi(v):
    if v >= 1e9:  return f"Rp {v/1e9:.2f}M"
    if v >= 1e6:  return f"Rp {v/1e6:.2f}JT"
    return f"Rp {v:,.0f}"

def fmt_num_kpi(v):
    if v >= 1e6: return f"{v/1e6:.1f}JT"
    return f"{v:,.0f}"

def format_idr_data(value: float) -> str:
    return f"Rp{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Digital Marketing Performance Optimization",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ═══════════════════════════════════════════════════════════════
# GLOBAL CSS
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    .stApp { background-color:#f0f4f8; }

    /* ── TAB STYLING: Hitam (Default), Merah (Active) ── */
    button[data-baseweb="tab"] p {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }
    button[aria-selected="true"] p {
        color: #EA4335 !important;
        font-weight: 800 !important;
    }
    button[aria-selected="true"] {
        border-bottom-color: #EA4335 !important;
    }

    /* ── sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#1e293b 0%,#0f172a 100%);
        width: 360px !important;
        min-width: 320px !important;
        padding: 18px 16px !important;
    }
    [data-testid="stSidebar"] * { color:#e2e8f0 !important; }

    .sidebar-title {
        text-align:center; padding:22px 12px 12px;
        font-size:1.35rem; font-weight:800; color:#f8fafc !important;
        border-bottom:1px solid #334155; margin-bottom:10px;
        white-space: normal; line-height:1.05; word-break:break-word; letter-spacing:0.2px;
    }
    .sidebar-subtitle {
        text-align:center; padding:0 16px 16px;
        font-size:0.75rem; color:#94a3b8 !important;
        text-transform:uppercase; letter-spacing:1.2px;
        white-space: normal;
    }

    /* ── KPI cards ── */
    .kpi-row { display:flex; gap:12px; flex-wrap:wrap; margin-bottom: 25px; }
    .kpi-card {
        background:#fff; border-radius:12px; padding:18px 20px;
        flex:1 1 200px; box-shadow:0 2px 8px rgba(0,0,0,.07);
        border-top:4px solid #4285F4;
    }
    .kpi-card.green  { border-top-color:#34A853; }
    .kpi-card.yellow { border-top-color:#FBBC04; }
    .kpi-card.red    { border-top-color:#EA4335; }
    .kpi-label { font-size:0.75rem; font-weight:600; text-transform:uppercase; color:#6b7280; }
    .kpi-value { font-size:1.6rem; font-weight:800; color:#1e293b; line-height:1.2; }
    .kpi-sub   { font-size:0.72rem; color:#9ca3af; margin-top:4px; }

    .section-header {
        font-size:1rem; font-weight:700; color:#000000; /* Warna Hitam */
        margin:22px 0 10px; padding-bottom:6px;
        border-bottom:2px solid #e5e7eb;
    }

    /* ── Insight Box Styling ── */
    .insight-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #EA4335;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-top: 15px;
        color: #000000 !important; /* Warna Hitam */
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════
@st.cache_data
def load_data():
    url = 'https://drive.google.com/uc?id=1lWFQMAN1tYENEnaOSdtUzG8AKPdAX_FR'
    df = pd.read_csv(url)
    df['created_date'] = pd.to_datetime(df['created_date'])
    for c in ['impressions','reach','clicks','link_clicks','content_views','add_to_cart','purchase']:
        if c in df.columns:
            df[c] = df[c].fillna(0).astype(int)
    parts = df['account_name'].str.split(' - ', n=1, expand=True)
    if parts.shape[1] > 1:
        df['industry'] = parts[1].fillna('Unknown')
    else:
        df['industry'] = 'Unknown'
    return df

df_raw = load_data()

# ═══════════════════════════════════════════════════════════════
# SIDEBAR FILTERS
# ═══════════════════════════════════════════════════════════════
st.sidebar.markdown('<div class="sidebar-title">📊 Digital Advertising<br>Performance &amp; Optimization Dashboard</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Deep Dive Analytics</div>', unsafe_allow_html=True)

min_d, max_d = df_raw['created_date'].min().date(), df_raw['created_date'].max().date()
date_range = st.sidebar.date_input("Rentang Tanggal", value=(min_d, max_d), label_visibility="collapsed")

sel_accounts = st.sidebar.multiselect("Account Name", sorted(df_raw['account_name'].unique()), default=sorted(df_raw['account_name'].unique()))
sel_objectives = st.sidebar.multiselect("Campaign Objective", sorted(df_raw['campaign_objective'].unique()), default=sorted(df_raw['campaign_objective'].unique()))
sel_industries = st.sidebar.multiselect("Industry", sorted(df_raw['industry'].unique()), default=sorted(df_raw['industry'].unique()))

df = df_raw.copy()
if len(date_range) == 2:
    df = df[(df['created_date'].dt.date >= date_range[0]) & (df['created_date'].dt.date <= date_range[1])]
df = df[df['account_name'].isin(sel_accounts)]
df = df[df['campaign_objective'].isin(sel_objectives)]
df = df[df['industry'].isin(sel_industries)]

# ═══════════════════════════════════════════════════════════════
# KPI SECTION
# ═══════════════════════════════════════════════════════════════
total_imp = df['impressions'].sum()
total_pv = df['purchase_value'].sum()
total_as = df['amount_spent'].sum()
roas_val = total_pv / total_as if total_as > 0 else 0
if not np.isfinite(roas_val):
    roas_val = 0
ctr_val = (df['clicks'].sum() / total_imp * 100) if total_imp > 0 else 0
if not np.isfinite(ctr_val):
    ctr_val = 0

# st.markdown('<div class="section-header">📈 Key Performance Indicators</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-label">Total Impressions</div>
    <div class="kpi-value">{fmt_num_kpi(total_imp)}</div>
    <div class="kpi-sub">Jumlah tayangan iklan</div>
  </div>
  <div class="kpi-card green">
    <div class="kpi-label">Total Purchase Value (Omzet)</div>
    <div class="kpi-value">{fmt_idr_kpi(total_pv)}</div>
    <div class="kpi-sub">{format_idr_data(total_pv)}</div>
  </div>
  <div class="kpi-card yellow">
    <div class="kpi-label">Total Amount Spent</div>
    <div class="kpi-value">{fmt_idr_kpi(total_as)}</div>
    <div class="kpi-sub">Biaya iklan total</div>
  </div>
  <div class="kpi-card red">
    <div class="kpi-label">Overall ROAS</div>
    <div class="kpi-value">{roas_val:.2f}x</div>
    <div class="kpi-sub">Return on Ad Spend</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Overall CTR</div>
    <div class="kpi-value">{ctr_val:.2f}%</div>
    <div class="kpi-sub">Click-Through Rate</div>
  </div>
</div>
""", unsafe_allow_html=True)

tab_perf, tab_trend, tab_industry, tab_strategic = st.tabs([
    "📊 Performance Metrics Analysis", 
    "📈 Trend & Time Series Analysis", 
    "🏭 Industry & Account Analysis",
    "🚀 Recommended Strategic Actions"
])

# ═══════════════════════════════════════════════════════════════
# TAB 1: PERFORMANCE
# ═══════════════════════════════════════════════════════════════
with tab_perf:
    st.markdown('<div class="section-header">CTR by Campaign Objective</div>', unsafe_allow_html=True)
    ctr_by_objective = df.groupby('campaign_objective').agg({'clicks': 'sum', 'impressions': 'sum'}).reset_index()
    ctr_by_objective['CTR'] = (ctr_by_objective['clicks'] / ctr_by_objective['impressions']) * 100
    fig_ctr = px.bar(ctr_by_objective, x='campaign_objective', y='CTR', color='campaign_objective', labels={'CTR': 'CTR (%)'}, color_discrete_sequence=['#4285F4', '#34A853'], hover_data=['clicks', 'impressions'], template='plotly_white')
    fig_ctr.update_traces(hovertemplate='<b>Campaign Objective</b>: %{x}<br><b>CTR</b>: %{y:.2f}%<br><b>Clicks</b>: %{customdata[0]:,.0f}<br><b>Impressions</b>: %{customdata[1]:,.0f}<extra></extra>')
    fig_ctr.update_layout(xaxis_title='Campaign Objective', yaxis_title='CTR (%)', hoverlabel=dict(bgcolor='white', bordercolor='black', font=dict(color='black')))
    st.plotly_chart(fig_ctr, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>CTR by Campaign Objective:</b><br><br>
        <b>Insight:</b> CTR luar biasa sebesar <b>9,98% (Traffic)</b> dan <b>9,88% (Sales)</b> membuktikan keunggulan visual serta akurasi penargetan iklan. 
        <br><br><b>Temuan Kritis:</b> menunjukkan adanya <b>bottleneck</b> pasca-klik karena tingginya minat audiens belum terkonversi menjadi profitabilitas (ROAS 0,81).
        <br><br><b>Rekomendasi Strategi:</b> Segera alihkan fokus dari eksperimen kreatif ke optimasi <b>Landing Page</b> dan alur <b>Checkout</b>, serta terapkan strategi <b>bundling</b> produk untuk meningkatkan <b>Average Order Value</b> (AOV).
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# TAB 2: TREND & TIME SERIES
# ═══════════════════════════════════════════════════════════════
with tab_trend:
    df['month'] = df['created_date'].dt.to_period('M').astype(str)
    kpi_trend = df.groupby('month').agg({'purchase_value': 'sum', 'amount_spent': 'sum', 'impressions': 'sum', 'reach': 'sum', 'clicks': 'sum'}).reset_index()

    # Guard ROAS and growth calculations to avoid division-by-zero and infinite values
    kpi_trend['roas'] = np.where(kpi_trend['amount_spent'] > 0, kpi_trend['purchase_value'] / kpi_trend['amount_spent'], 0)
    kpi_trend['roas_growth'] = kpi_trend['roas'].pct_change() * 100
    kpi_trend['ctr'] = np.where(kpi_trend['impressions'] > 0, (kpi_trend['clicks'] / kpi_trend['impressions']) * 100, 0)
    kpi_trend['ctr_growth'] = kpi_trend['ctr'].pct_change() * 100
    kpi_trend['pv_growth'] = kpi_trend['purchase_value'].pct_change() * 100
    kpi_trend['as_growth'] = kpi_trend['amount_spent'].pct_change() * 100
    # Replace inf values produced by pct_change when dividing by zero
    kpi_trend.replace([np.inf, -np.inf], np.nan, inplace=True)
    kpi_trend = kpi_trend.fillna(0)

    google_colors = ['#4285F4', '#34A853', '#FBBC05', '#EA4335']

    # --- Chart 1: PV, AS & Growth ---
    st.markdown('<div class="section-header">Monthly Trend: Purchase Value, Amount Spent, PV Growth (%), and AS Growth (%)</div>', unsafe_allow_html=True)
    kpi_trend['formatted_pv'] = kpi_trend['purchase_value'].apply(format_idr_data)
    kpi_trend['formatted_as'] = kpi_trend['amount_spent'].apply(format_idr_data)
    common_data = kpi_trend[['formatted_pv', 'formatted_as', 'pv_growth', 'as_growth']].values

    fig_pv_as = make_subplots(specs=[[{"secondary_y": True}]])
    fig_pv_as.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['purchase_value'], name='Purchase Value', mode='markers+lines', line=dict(color=google_colors[1]), customdata=common_data,
                                   hovertemplate='<b>Purchase Value</b>: %{customdata[0]}<br><b>PV Growth</b>: %{customdata[2]:.2f}%<extra></extra>'), secondary_y=False)
    fig_pv_as.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['amount_spent'], name='Amount Spent', mode='markers+lines', line=dict(color=google_colors[3]), customdata=common_data,
                                   hovertemplate='<b>Amount Spent</b>: %{customdata[1]}<br><b>AS Growth</b>: %{customdata[3]:.2f}%<extra></extra>'), secondary_y=False)
    fig_pv_as.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['pv_growth'], name='PV Growth (%)', mode='markers+lines', line=dict(color=google_colors[1], dash='dash'), hoverinfo='skip', showlegend=True), secondary_y=True)
    fig_pv_as.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['as_growth'], name='AS Growth (%)', mode='markers+lines', line=dict(color=google_colors[3], dash='dash'), hoverinfo='skip', showlegend=True), secondary_y=True)
    fig_pv_as.update_layout(title_text=None, hovermode='x unified', template='plotly_white')
    fig_pv_as.update_xaxes(title_text='month')
    fig_pv_as.update_yaxes(title_text="Total Purchase Value and Advertising Spend (Rp)", secondary_y=False, rangemode='tozero')
    st.plotly_chart(fig_pv_as, use_container_width=True)

    # --- Chart 2: CTR Trend ---
    st.markdown('<div class="section-header">Monthly Trend: CTR (%) and CTR Growth (%)</div>', unsafe_allow_html=True)
    fig_ctr_trend = make_subplots(specs=[[{"secondary_y": True}]])
    fig_ctr_trend.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['ctr'], name='CTR (%)', mode='markers+lines', line=dict(color=google_colors[1])), secondary_y=False)
    fig_ctr_trend.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['ctr_growth'], name='CTR Growth (%)', mode='markers+lines', line=dict(color='#4285F4', dash='dash')), secondary_y=True)
    fig_ctr_trend.update_layout(title_text=None, hovermode="x unified", template='plotly_white')
    fig_ctr_trend.update_xaxes(title_text='month')
    fig_ctr_trend.update_yaxes(title_text="CTR (%)", secondary_y=False)
    fig_ctr_trend.update_traces(hovertemplate='<b>CTR</b>: %{y:.2f}%<extra></extra>', selector=dict(name='CTR (%)'))
    fig_ctr_trend.update_traces(hovertemplate='<b>CTR Growth</b>: %{y:.2f}%<extra></extra>', selector=dict(name='CTR Growth (%)'))
    st.plotly_chart(fig_ctr_trend, use_container_width=True)

    # --- Chart 3: ROAS Trend ---
    st.markdown('<div class="section-header">Monthly Trend: ROAS and ROAS Growth (%)</div>', unsafe_allow_html=True)
    fig_roas_trend = make_subplots(specs=[[{"secondary_y": True}]])
    fig_roas_trend.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['roas'], name='ROAS', mode='markers+lines', line=dict(color=google_colors[2])), secondary_y=False)
    fig_roas_trend.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['roas_growth'], name='ROAS Growth (%)', mode='markers+lines', line=dict(color='white', dash='dash', width=3)), secondary_y=True)
    fig_roas_trend.update_layout(title_text=None, hovermode="x unified", template='plotly_white')
    fig_roas_trend.update_xaxes(title_text='month')
    fig_roas_trend.update_yaxes(title_text="ROAS (%)", secondary_y=False)
    fig_roas_trend.update_traces(hovertemplate='<b>ROAS</b>: %{y:.2f}x<extra></extra>', selector=dict(name='ROAS'))
    fig_roas_trend.update_traces(hovertemplate='<b>ROAS Growth</b>: %{y:.2f}%<extra></extra>', selector=dict(name='ROAS Growth (%)'))
    st.plotly_chart(fig_roas_trend, use_container_width=True)

    # --- Chart 4: IRC Trend ---
    st.markdown('<div class="section-header">Monthly Trend: Impressions, Reach, and Clicks</div>', unsafe_allow_html=True)
    fig_irc = go.Figure()
    fig_irc.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['impressions'], name='Impressions', mode='markers+lines', line=dict(color=google_colors[0])))
    fig_irc.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['reach'], name='Reach', mode='markers+lines', line=dict(color=google_colors[1])))
    fig_irc.add_trace(go.Scatter(x=kpi_trend['month'], y=kpi_trend['clicks'], name='Clicks', mode='markers+lines', line=dict(color=google_colors[2])))
    fig_irc.update_layout(title_text=None, hovermode="x unified", template='plotly_white')
    fig_irc.update_xaxes(title_text='month')
    fig_irc.update_yaxes(title_text="Count")
    fig_irc.update_traces(hovertemplate='<b>%{fullData.name}</b>: %{y:,.0f}<extra></extra>')
    st.plotly_chart(fig_irc, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>Trend & Time Series Analysis:</b><br><br>
        <b>Insight:</b> Analisis tren mengonfirmasi pola musiman yang kuat dengan puncak performa pada <b>April 2023 (naik 109,71% MoM)</b> 
        dan kuartal akhir tahun, yang dipicu oleh momentum Lebaran serta festival belanja. 
        <br><br><b>Temuan Kritis:</b> Di luar periode puncak, efisiensi biaya sering melemah karena kenaikan <i>Amount Spent</i> 
        tidak dibarengi pertumbuhan omzet yang proporsional. 
        <br><br><b>Rekomendasi Strategi:</b> Terapkan <i>Aggressive Scaling</i> anggaran dua minggu sebelum April dan Oktober untuk memaksimalkan lonjakan daya beli, serta lakukan 
        <i>Budget Re-allocation</i> pada bulan-bulan stagnan guna menjaga stabilitas margin profitabilitas agensi.
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# TAB 3: INDUSTRY & ACCOUNT ANALYSIS
# ═══════════════════════════════════════════════════════════════
with tab_industry:
    st.markdown('<div class="section-header">Highest Average Purchase Value by Industry</div>', unsafe_allow_html=True)
    avg_pv_ind = df.groupby('industry')['purchase_value'].mean().reset_index().sort_values(by='purchase_value', ascending=False)
    fig_avg_pv = px.bar(avg_pv_ind, x='industry', y='purchase_value', color='industry', color_discrete_map={'Beauty': '#4285F4', 'Fashion': '#34A853', 'FMCG': '#FBBC04'}, template='plotly_white')
    fig_avg_pv.update_layout(yaxis=dict(title='Rata-Rata Omzet'), hovermode='x unified')
    fig_avg_pv.update_traces(hovertemplate='<b>Industry</b>: %{x}<br><b>Rata-Rata Omzet</b>: Rp%{y:,.0f}<extra></extra>')
    st.plotly_chart(fig_avg_pv, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>Highest Average Purchase Value by Industry:</b><br><br>
        <b>Insight:</b> Industri <b>Beauty</b> memimpin tipis dengan nilai rata-rata omzet tertinggi sebesar <b>Rp 2.398.943</b>, mengungguli Fashion dan FMCG. Dominasi ini mengindikasikan kualitas transaksi yang lebih premium dan audiens yang lebih loyal terhadap nilai produk tinggi (High-Value Customers).
        <br><br><b>Temuan Kritis:</b> Meskipun industri Beauty memiliki potensi pendapatan per transaksi terbesar, selisih antar industri yang sangat kecil menunjukkan bahwa efisiensi iklan di sektor lain sebenarnya hampir setara.
        <br><br><b>Rekomendasi Strategi:</b> Optimalkan profitabilitas dengan menerapkan strategi <b>cross-selling</b> dan <b>bundling</b> produk premium khusus pada kampanye industri Beauty guna memperlebar margin AOV, serta replikasi formula copywriting bernilai tinggi tersebut ke industri Fashion untuk mengejar ketertinggalan omzet rata-rata.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Account-Level Comparison: Purchase Value vs Amount Spent</div>', unsafe_allow_html=True)
    acc_stats = df.groupby('account_name').agg({'purchase_value': 'sum', 'amount_spent': 'sum'}).reset_index().sort_values(by='purchase_value', ascending=False)
    acc_stats['formatted_pv'] = acc_stats['purchase_value'].apply(format_idr_data)
    acc_stats['formatted_as'] = acc_stats['amount_spent'].apply(format_idr_data)
    fig_acc = go.Figure()
    fig_acc.add_trace(go.Bar(name='Purchase Value', x=acc_stats['account_name'], y=acc_stats['purchase_value'], marker_color='#34A853', customdata=acc_stats[['formatted_pv', 'formatted_as']].values, hovertemplate='<b>%{x}</b><br><b>Purchase Value</b>: %{customdata[0]}<extra></extra>'))
    fig_acc.add_trace(go.Bar(name='Amount Spent', x=acc_stats['account_name'], y=acc_stats['amount_spent'], marker_color='#EA4335', customdata=acc_stats[['formatted_pv', 'formatted_as']].values, hovertemplate='<b>%{x}</b><br><b>Amount Spent</b>: %{customdata[1]}<extra></extra>'))
    fig_acc.update_layout(barmode='group', hovermode='x unified', template='plotly_white', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    fig_acc.update_yaxes(title_text="Jumlah (Rp)")
    st.plotly_chart(fig_acc, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>Account-Level Comparison: Purchase Value vs Amount Spent:</b><br><br>
        <b>Insight:</b> <b>Client C - Fashion</b> memimpin sebagai brand paling efektif dengan perolehan omzet tertinggi mencapai <b>Rp 1,77 Miliar</b>, disusul ketat oleh Client D dan Client B dari industri Beauty. Skala pendapatan ini membuktikan dominasi akun-akun tersebut sebagai penggerak utama volume transaksi agensi. 
        <br><br><b>Temuan Kritis:</b> Meskipun mencatatkan omzet jumbo, seluruh brand di posisi teratas memiliki beban biaya iklan (Amount Spent) yang melampaui pendapatan kotor yang dihasilkan, di mana Client C memerlukan biaya Rp 2,12 Miliar untuk mencapai omzet tersebut.
        <br><br><b>Rekomendasi Strategi:</b> Segera alihkan fokus dari sekadar mengejar volume penjualan ke efisiensi beban operasional dengan melakukan audit ketat pada biaya akuisisi per pelanggan dan menaikkan Average Order Value (AOV) agar pertumbuhan omzet ke depan tidak lagi terbebani oleh pengeluaran iklan yang membengkak.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Highest ROAS by Industry</div>', unsafe_allow_html=True)
    roas_ind = df.groupby('industry').agg({'purchase_value': 'sum', 'amount_spent': 'sum'}).reset_index()
    roas_ind['ROAS'] = roas_ind['purchase_value'] / roas_ind['amount_spent']
    roas_ind = roas_ind.sort_values(by='ROAS', ascending=False)
    roas_ind['f_pv'] = roas_ind['purchase_value'].apply(format_idr_data)
    roas_ind['f_as'] = roas_ind['amount_spent'].apply(format_idr_data)
    fig_roas = px.bar(roas_ind, x='industry', y='ROAS', color='industry', color_discrete_map={'Beauty': '#34A853', 'Fashion': '#4285F4', 'FMCG': '#FBBC05'}, custom_data=[roas_ind['f_pv'], roas_ind['f_as']])
    fig_roas.update_layout(yaxis_title='ROAS (x)', hovermode='x unified')
    fig_roas.update_traces(hovertemplate='<b>Industry</b>: %{x}<br><b>ROAS</b>: %{y:.2f}x<br><b>Purchase Value</b>: %{customdata[0]}<br><b>Amount Spent</b>: %{customdata[1]}<extra></extra>')
    st.plotly_chart(fig_roas, use_container_width=True)

    st.markdown(f"""
    <div class="insight-box">
        <b>Highest ROAS by Industry:</b><br><br>
        <b>Insight:</b> Industri <b>Beauty</b> mencatatkan efisiensi iklan terbaik dengan ROAS tertinggi sebesar <b>0,81x</b>, didorong oleh perolehan omzet (Purchase Value) sebesar <b>Rp3,50 Miliar</b> dari beban biaya (Amount Spent) <b>Rp4,30 Miliar</b>. Angka ini mengungguli FMCG (ROAS 0,81x) dan Fashion (ROAS 0,80x) yang memiliki beban pengeluaran tertinggi namun hasil terendah. 
        <br><br><b>Temuan Kritis:</b> Meskipun Beauty memimpin, fakta bahwa seluruh industri memiliki ROAS < 1,00x menunjukkan adanya masalah profitabilitas sistemik di mana pengeluaran iklan selalu lebih besar daripada pendapatan yang dihasilkan.
        <br><br><b>Rekomendasi Strategi:</b> Prioritaskan audit mendalam pada kampanye Beauty untuk menemukan elemen pendorong efisiensi, lalu lakukan replikasi strategi tersebut ke industri Fashion dengan pengetatan target cost per acquisition (CPA) guna memastikan seluruh portofolio segera mencapai titik impas (break-even) dan profitabilitas di atas 100%.
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# TAB 4: RECOMMENDED STRATEGIC ACTIONS
# ═══════════════════════════════════════════════════════════════
with tab_strategic:
    st.markdown('<div class="section-header" style="color: #000000 !important;">🚀 RECOMMENDED STRATEGIC ACTIONS</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="insight-box" style="color: #000000 !important;">
        <h3 style="color: #000000; margin:0;">Executive Summary & Strategy Plan</h3><br>
        Berdasarkan analisis komprehensif, agensi memiliki keunggulan daya tarik iklan (CTR 9,93%), namun menghadapi tantangan profitabilitas (ROAS 0,81x). 
        Strategi utama harus bergeser dari sekadar mengejar volume klik menjadi <b>optimalisasi efisiensi konversi pasca-klik</b>.
    </div>
    """, unsafe_allow_html=True)

    # --- 1. Post-Click Optimization ---
    st.markdown(f"""
    <div class="insight-box" style="color: #000000 !important;">
        <h4 style="color: #000000; margin:0;">1. Optimalisasi Pasca-Klik (Mengatasi "Kebocoran" Funnel)</h4><br>
        <b>Temuan Kritis:</b> Meskipun CTR sangat tinggi (9,93%), rendahnya ROAS mengindikasikan audiens yang tertarik klik iklan gagal berkonversi menjadi pembeli profitabel. Bottleneck ada pada tahapan post-click.<br><br>
        <b>Tindakan Strategis:</b><br>
        • Lakukan audit menyeluruh pada UX Landing Page (A/B Testing headline, visual, dan CTA).<br>
        • Sederhanakan proses Checkout (Guest checkout, biaya transparan di awal).<br>
        • Implementasi strategi Upselling & Cross-selling pada produk industri Beauty untuk meningkatkan Average Order Value (AOV).
    </div>
    """, unsafe_allow_html=True)

    # --- 2. Budget Allocation ---
    st.markdown(f"""
    <div class="insight-box" style="color: #000000 !important;">
        <h4 style="color: #000000; margin:0;">2. Optimalisasi Anggaran (Memaksimalkan Peluang Musiman)</h4><br>
        <b>Temuan Kritis:</b> Lonjakan pertumbuhan omzet tajam terjadi pada April (109,71% MoM) dan Q4. Sebaliknya, biaya iklan sering membengkak tanpa kenaikan omzet proporsional di bulan stagnan.<br><br>
        <b>Tindakan Strategis:</b><br>
        • Terapkan <b>Aggressive Scaling</b> anggaran pada H-14 periode puncak musiman.<br>
        • Lakukan alokasi anggaran lebih besar ke industri <b>Beauty</b> dan brand <b>Client C - Fashion</b> yang memiliki efisiensi relatif lebih baik.<br>
        • Stop kampanye dengan ROAS sangat rendah dan pindahkan anggaran ke segmen berdaya beli tinggi.
    </div>
    """, unsafe_allow_html=True)

    # --- 3. Replication Success ---
    st.markdown(f"""
    <div class="insight-box" style="color: #000000 !important;">
        <h4 style="color: #000000; margin:0;">3. Ekstraksi & Replikasi Strategi Berkinerja Tinggi</h4><br>
        <b>Temuan Kritis:</b> Brand pendorong pendapatan utama (Client C - Fashion) dan Industri Beauty memiliki aset kreatif yang berhasil memancing omzet besar.<br><br>
        <b>Tindakan Strategis:</b><br>
        • Lakukan studi kasus internal pada Client C untuk mengidentifikasi "Winning Creative" dan replikasi formulanya ke brand lain.<br>
        • Standardisasi proses penargetan audiens hangat berdasarkan pembelajaran dari industri Beauty.<br>
        • Gunakan benchmark CTR 9.9% sebagai target standar baru kualitas kreatif seluruh tim.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight-box" style="color: #000000 !important;">
        💡 <strong>Final Goal:</strong> Mengubah investasi iklan dari beban operasional menjadi penggerak profit berkelanjutan dengan target ROAS portofolio &gt; 1.25x.
    </div>
    """, unsafe_allow_html=True)