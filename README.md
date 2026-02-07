# 📊 Digital Advertising Performance Optimization Dashboard

<div align="center">

![Dashboard Banner](https://img.shields.io/badge/Analytics-Deep%20Dive-4285F4?style=for-the-badge&logo=google-analytics&logoColor=white)

**Transforming Ad Spend into Profitable Business Growth**

[![Live Demo](https://img.shields.io/badge/Demo-Live-success?style=for-the-badge)](https://digital-advertising-performance-optimization-dashboard.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

</div>

---

## 📊 Tentang Proyek

Dashboard analitik komprehensif untuk mengoptimalkan **performa kampanye iklan digital** lintas industri (Beauty, Fashion, FMCG). Platform ini dirancang untuk membantu digital marketing agencies dan business owners dalam mengubah pengeluaran iklan menjadi pertumbuhan bisnis yang terukur dan profitable.

### 🎯 **Latar Belakang**

Dalam lanskap digital marketing yang semakin kompetitif, banyak bisnis menghadapi paradoks:
- **High Click-Through Rate (CTR)** namun **Low Conversion**
- **Massive Ad Spend** tanpa **Return on Investment (ROI)** yang sehat
- **Lack of Visibility** tentang performa kampanye secara menyeluruh

Dashboard ini lahir dari kebutuhan untuk memberikan **transparansi penuh** atas efektivitas setiap rupiah yang diinvestasikan dalam iklan digital, dengan fokus pada **actionable insights** yang dapat langsung diterapkan untuk meningkatkan profitabilitas.

### 💡 **Business Problem**

Agensi digital marketing menghadapi tantangan kritis dalam mengelola portofolio iklan klien:

**Masalah Utama:**
1. **Profitability Crisis** - ROAS keseluruhan 0.81x (setiap Rp 1 yang dikeluarkan hanya menghasilkan Rp 0.81)
2. **Conversion Bottleneck** - CTR sangat tinggi (9.93%) namun tidak terkonversi menjadi penjualan yang profitable
3. **Budget Inefficiency** - Pengeluaran iklan membengkak tanpa peningkatan omzet proporsional
4. **Lack of Standardization** - Tidak ada formula replikasi sukses antar kampanye/brand

**Dampak Bisnis:**
- Kerugian akumulatif dari ad spend yang tidak efisien
- Margin profit agensi tertekan
- Risiko kehilangan kepercayaan klien
- Ketergantungan pada trial-error tanpa data-driven decision

Dashboard ini membantu stakeholder untuk:
- **Mengidentifikasi campaign winners** untuk direplikasi strateginya
- **Mendeteksi performance leakage** di funnel untuk immediate action
- **Mengoptimalkan budget allocation** berbasis ROI per industri/brand
- **Meningkatkan ROAS** melalui post-click optimization yang terukur

---

## 🎯 Tujuan Bisnis

Dashboard ini menjawab **4 Pertanyaan Bisnis Kritis**:

| Area Analisis | Pertanyaan Bisnis | Metrik Kunci | Tujuan |
|---------------|-------------------|--------------|--------|
| **Performance Metrics** | Seberapa efektif iklan dalam menarik engagement audiens? | CTR, Impressions, Clicks | Evaluasi daya tarik kreatif iklan |
| **Trend & Time Series** | Kapan momentum terbaik untuk aggressive scaling? | Monthly ROAS, Purchase Value Growth, CTR Growth | Identifikasi pola musiman untuk budget optimization |
| **Industry & Account** | Brand/industri mana yang paling efisien dan profitable? | ROAS per Industry, Average Purchase Value, Account Performance | Portfolio prioritization & resource allocation |
| **Strategic Actions** | Apa langkah konkrit untuk mencapai ROAS > 1.25x? | Post-Click Conversion, AOV, Budget Efficiency | Roadmap untuk sustainable profitability |

---

## 📈 Analisis Bisnis

### **1. Performance Metrics Analysis**

#### **CTR by Campaign Objective**

**Key Metrics:**
- **Traffic Campaign CTR**: 9.98%
- **Sales Campaign CTR**: 9.88%
- **Overall CTR**: 9.93%

**Finding Kritis:**
- CTR **luar biasa tinggi** (9.93%) membuktikan keunggulan visual dan akurasi targeting
- **Paradox Alert**: Tingginya minat klik belum terkonversi menjadi profitabilitas (ROAS 0.81x)
- Indikasi kuat adanya **bottleneck pasca-klik** di landing page atau checkout flow

**Business Impact:**
> Agensi sudah menguasai seni "menarik perhatian" audiens, namun gagal "menutup penjualan". Fokus harus segera bergeser dari eksperimen kreatif ke optimasi konversi pasca-klik.

**Benchmark Industry:**
- CTR rata-rata industri e-commerce: 2-3%
- CTR agensi: **9.93%** (outperform 3-4x lipat)
- **Gap**: Opportunity lost akibat conversion rate yang tidak sebanding

---

### **2. Trend & Time Series Analysis**

#### **Monthly Performance Trends**

**Puncak Performa:**
- **April 2023**: Purchase Value growth **+109.71% MoM**
- **Q4 2023**: Lonjakan konsisten karena festival belanja akhir tahun
- **Maret-Mei**: Window momentum Lebaran yang harus dimaksimalkan

**Periode Stagnan:**
- **Januari-Februari**: Growth melambat, efficiency drop
- **Juni-Agustus**: Flat performance dengan high ad spend

**Finding Kritis:**
- **Pola Musiman Kuat**: Performa sangat dipengaruhi seasonal momentum (Ramadan, Year-End Sale)
- **Budget Inefficiency**: Di luar periode puncak, kenaikan Amount Spent tidak dibarengi growth omzet proporsional
- **Missed Opportunity**: Tidak ada aggressive scaling 2 minggu sebelum puncak musiman

**Business Impact:**
> Tanpa seasonal budget planning yang tepat, agensi kehilangan 40-50% potensi revenue di periode high-demand dan membuang budget di periode low-efficiency.

**ROAS Volatility:**
```
ROAS Tertinggi: 1.2x (April 2023) ✅
ROAS Terendah: 0.6x (Agustus 2023) 🔴
Target Sustainable: > 1.25x
```

---

### **3. Industry & Account Analysis**

#### **Average Purchase Value by Industry**

**Top Performers:**
1. 🥇 **Beauty** - Rp 2.398.943 (Premium transactions)
2. 🥈 **Fashion** - Rp 2.380.000 (Volume leader)
3. 🥉 **FMCG** - Rp 2.350.000 (Consistent baseline)

**Finding Kritis:**
- **Beauty dominates quality**: Highest AOV dengan customer base yang lebih loyal
- **Selisih minimal** antar industri (< 3%) menunjukkan potensi setara jika dioptimalkan
- **High-Value Customer Concentration**: Peluang premium pricing & bundling di Beauty

**Business Impact:**
> Industri Beauty memiliki "proven formula" untuk transaksi bernilai tinggi yang dapat direplikasi ke Fashion & FMCG untuk mengejar ketertinggalan AOV.

---

#### **Account-Level Performance**

**Revenue Leaders:**
1. 🏆 **Client C - Fashion**: Rp 1.77 Miliar (Revenue champion)
2. 🥈 **Client D - Beauty**: Rp 1.65 Miliar
3. 🥉 **Client B - Beauty**: Rp 1.50 Miliar

**Cost Reality Check:**
- **Client C** menghasilkan Rp 1.77B dengan biaya **Rp 2.12B** (ROAS 0.83x)
- **Client D** menghasilkan Rp 1.65B dengan biaya **Rp 2.05B** (ROAS 0.80x)

**Finding Kritis:**
- 🚨 **Volume ≠ Profitability**: Brand top revenue masih beroperasi di bawah break-even
- 💸 **Cost Bloat**: Semua top accounts memiliki ad spend > purchase value
- ⚠️ **Sustainability Risk**: Model bisnis current tidak sustainable dalam jangka panjang

**Business Impact:**
> Mengejar volume penjualan tanpa efisiensi biaya adalah resep kerugian. Perlu pivot dari "revenue maximization" ke "profit optimization".

---

#### **ROAS by Industry**

**Efficiency Ranking:**
1. 🥇 **Beauty**: 0.81x (Rp 3.50B revenue / Rp 4.30B spend)
2. 🥈 **FMCG**: 0.81x
3. 🥉 **Fashion**: 0.80x (Rp 3.67B revenue / Rp 4.59B spend)

**Finding Kritis:**
- **Beauty leads efficiency** meskipun masih sub-optimal (< 1.0x)
- **Sistemik Problem**: SEMUA industri ROAS < 1.0x (unprofitable)
- **Fashion paradox**: Volume revenue tertinggi, efficiency terendah

**Business Impact:**
> Ini bukan masalah satu brand, ini adalah **krisis profitabilitas sistemik** yang memerlukan overhaul strategi menyeluruh di seluruh portfolio.

---

## 🔍 Key Findings

### 🚨 **Crisis Indicators**

1. **Profitability Crisis**
   - ROAS portfolio 0.81x (EVERY Rp 1 spent → Rp 0.81 return)
   - ZERO industry mencapai break-even (ROAS 1.0x)
   - Accumulated loss dari inefficient ad spend

2. **Conversion Bottleneck**
   - CTR 9.93% (EXCELLENT) vs ROAS 0.81x (POOR)
   - Massive drop-off antara click → purchase
   - Post-click experience failure

3. **Budget Misallocation**
   - Ad spend meningkat di periode low-demand
   - Underinvestment saat seasonal peak (April, Q4)
   - No dynamic budget reallocation mechanism

4. **Lack of Best Practice Replication**
   - Winning campaigns tidak ter-standardisasi
   - Setiap brand "start from scratch"
   - Knowledge tidak ter-transfer antar account

---

## 💡 Rekomendasi Strategis

### 🎯 **Prioritas 1: Post-Click Optimization (Mengatasi "Kebocoran" Funnel)**

**Temuan Kritis:**
> CTR 9.93% namun ROAS 0.81x = Audiens tertarik klik, tapi gagal beli. Masalah ada PASCA-klik.

**Aksi Strategis:**

**A. Landing Page Overhaul**
1. **A/B Testing Agresif**
   - Test 3 variasi headline per minggu
   - Optimize hero image untuk mobile (80% traffic)
   - Simplify form (max 3 fields)

2. **Speed Optimization**
   - Target: < 2 detik load time
   - Compress images, lazy loading
   - CDN implementation

3. **Trust Signals**
   - Tampilkan testimonial real customer
   - Security badges (SSL, payment methods)
   - Money-back guarantee prominent

**B. Checkout Flow Simplification**
1. **Guest Checkout** (reduce friction)
2. **Transparansi Biaya** di awal (no surprise fees)
3. **Progress Indicator** (show steps remaining)
4. **Multiple Payment Options** (e-wallet, BNPL)

**C. Average Order Value (AOV) Boost**
1. **Bundling Strategy**
   - Beauty: Skincare routine sets (discount 15%)
   - Fashion: Mix & match outfits
   - FMCG: Bulk purchase incentives

2. **Upselling at Checkout**
   - "Customers also bought..."
   - "Complete your look with..."

3. **Free Shipping Threshold**
   - Set di Rp 250K (push from Rp 238K average)

**Expected Impact:**
- ROAS increase: 0.81x → 1.10x (+35%)
- Revenue increase: +25% tanpa extra ad spend
- Conversion rate improvement: +40%

**Timeline:** 30-45 hari

---

### 💰 **Prioritas 2: Budget Allocation Optimization (Maksimalkan Peluang Musiman)**

**Temuan Kritis:**
> April growth +109.71% MoM, tapi tidak ada aggressive scaling pre-event. Budget terbuang di bulan stagnan.

**Aksi Strategis:**

**A. Seasonal Scaling Strategy**
1. **H-14 Aggressive Scaling**
   - Identify peak: Ramadan (Maret-April), Year-End (Nov-Des)
   - Increase budget 150-200% di H-14
   - Focus pada winning creatives

2. **Budget Calendar Template**
   ```
   Januari-Februari: 70% baseline budget (conservation mode)
   Maret-April: 200% budget (Ramadan boost)
   Mei-Agustus: 80% baseline
   September-Desember: 180% budget (Year-end festivals)
   ```

**B. Industry Budget Reallocation**
1. **Prioritize Beauty** (ROAS leader 0.81x)
   - Alokasi 45% total budget (dari 33% current)
   
2. **Optimize Fashion** (volume leader)
   - Maintain 40% budget
   - Focus pada efficiency improvement
   
3. **FMCG** (stable baseline)
   - 15% budget for testing

**C. Stop Low-Performing Campaigns**
- **Kill threshold**: ROAS < 0.5x selama 2 minggu
- **Redirect budget**: ke campaigns ROAS > 0.9x
- **Review cycle**: Weekly performance audit

**Expected Impact:**
- Cost reduction: -20% wasted spend
- ROAS improvement: 0.81x → 1.05x
- Seasonal revenue boost: +60% vs current

**Timeline:** Immediate implementation (next campaign cycle)

---

### 📋 **Prioritas 3: Winning Formula Replication**

**Temuan Kritis:**
> Client C - Fashion sukses Rp 1.77B, tapi formula tidak ter-standardisasi ke brand lain.

**Aksi Strategis:**

**A. Internal Case Study (Client C - Fashion)**
1. **Creative Audit**
   - Identify top 10 best-performing ads
   - Breakdown: Visual style, copywriting tone, CTA
   - Create "Creative Playbook"

2. **Audience Targeting Blueprint**
   - Document winning audience segments
   - Interest combinations yang convert
   - Custom audience strategy

3. **Campaign Structure Template**
   - Budget distribution model
   - Ad set hierarchy
   - Bidding strategy yang proven

**B. Cross-Brand Knowledge Transfer**
1. **Monthly Best Practice Sharing**
   - Showcase winning campaigns
   - "What worked, what didn't" session
   - Share creative assets

2. **Standardized Metrics Dashboard**
   - ALL accounts track same KPIs
   - Unified reporting format
   - Benchmark comparison

**C. CTR 9.9% as New Standard**
- Use current CTR as quality threshold
- Reject creatives < 5% CTR in testing
- Continuous creative iteration

**Expected Impact:**
- Faster campaign setup: -50% time
- Consistent performance: All brands ROAS > 0.9x
- Reduced testing cost: -30%

**Timeline:** 60 hari (documentation + training)

---

### 🚀 **Prioritas 4: Profitability Mindset Shift**

**Temuan Kritis:**
> Agensi terbiasa ukur sukses dari "revenue generated" bukan "profit margin". Perlu culture shift.

**Aksi Strategis:**

**A. New Success Metrics**
```
OLD: Total Purchase Value (Omzet)
NEW: Net Profit from Ads (Purchase Value - Amount Spent - Operational Cost)

OLD: Client with highest revenue
NEW: Client with highest ROAS & sustainment
```

**B. Client Education Program**
1. **ROAS Transparency Report**
   - Monthly profit/loss statement per campaign
   - Show TRUE cost of acquisition
   - Educate pada sustainable growth

2. **Tiered Pricing Model**
   - Premium fee untuk ROAS > 1.5x achievements
   - Penalty/discount untuk persistent ROAS < 0.8x
   - Align incentives dengan profitability

**C. Portfolio Target (12 Bulan)**
```
Current State:
- ROAS Portfolio: 0.81x 🔴
- Profitable Accounts: 0/10

Target State:
- ROAS Portfolio: > 1.25x ✅
- Profitable Accounts: 7/10 (70%)
- Premium Accounts (ROAS > 1.5x): 3/10 (30%)
```

**Expected Impact:**
- 💰 Agensi margin: +45%
- 🤝 Client retention: +30% (proven ROI)
- 🏆 Industry positioning: "Profit-focused agency"

---

## 📊 Business Metrics Dashboard

### **Current State (Baseline)**

| Metric | Value | Status |
|--------|-------|--------|
| Overall ROAS | 0.81x | 🔴 Unprofitable |
| Overall CTR | 9.93% | 🟢 Excellent |
| Avg Purchase Value | Rp 2.38JT | 🟡 Good |
| Monthly Revenue | Rp 1.5B - 3.2B | 🟡 Volatile |
| Ad Spend Efficiency | Setiap Rp 1 → Rp 0.81 | 🔴 Critical |
| Profitable Industries | 0/3 | 🔴 Critical |

### **Target State (6-12 Bulan)**

| Metric | Target | Growth Required |
|--------|--------|----------------|
| Overall ROAS | > 1.25x | ⬆️ +54% |
| Profitable Industries | 3/3 (100%) | ⬆️ +100% |
| Avg Purchase Value | > Rp 3.0JT | ⬆️ +26% |
| Ad Spend Efficiency | Setiap Rp 1 → Rp 1.25+ | ⬆️ +54% |
| Client Retention Rate | > 85% | ⬆️ +20% |
| Monthly Profit Margin | > 20% | NEW |

---

## 🎓 Metodologi

### **Data Sources**
- **Campaign Performance Data** (2023-2024)
  - Platform: Meta Ads (Facebook/Instagram)
  - Metrics: Impressions, Reach, Clicks, Conversions
  - Financial: Amount Spent, Purchase Value

- **Account & Industry Segmentation**
  - 10 Client Accounts across 3 industries
  - Campaign Objectives: Traffic, Sales, Engagement

### **Analysis Framework**
1. **Descriptive Analytics**: Current state assessment (What happened?)
2. **Diagnostic Analytics**: Root cause identification (Why it happened?)
3. **Prescriptive Analytics**: Strategic recommendations (What should we do?)
4. **Predictive Elements**: Trend forecasting untuk seasonal planning

### **Key Assumptions**
- ROAS sebagai proxy utama profitabilitas campaign
- CTR sebagai proxy daya tarik kreatif
- Purchase Value sebagai proxy customer lifetime value
- Industry benchmarking untuk relative performance assessment

### **Visualization Approach**
- **Google Colors Palette** untuk consistency (Blue, Green, Yellow, Red)
- **Indonesian Format** (Rp, JT, M, RB) untuk local context
- **Interactive Plotly Charts** dengan detailed hover information
- **Multi-axis Time Series** untuk trend correlation analysis

---

## 👥 Tim Deep Dive Analytics

<div align="center">

### **Contributors**

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/FarrelllAdityaaa.png" width="100px;" alt="Farrel Paksi Aditya"/><br />
      <sub><b>Farrel Paksi Aditya</b></sub><br />
      <sub>🧑🏻‍💻 Data Analyst & Business Intelligence</sub>
    </td>
    <td align="center">
      <img src="https://github.com/NabilaPutriAsySyifa.png" width="100px;" alt="Nabila Putri Asy Syifa"/><br />
      <sub><b>Nabila Putri Asy Syifa</b></sub><br />
      <sub>👩🏻‍💻 Data Analyst & Strategic Planning</sub>
    </td>
  </tr>
</table>

**Independent Analytics Project - 2025**

*Transforming complex advertising data into actionable business strategies*

</div>

---

## 📞 Kontak

- Email: nabilaputriasysyifa99@gmail.com
- LinkedIn: [Nabila Putri Asy Syifa](https://www.linkedin.com/in/nabila-putri-asy-syifa)
- LinkedIn: [Farrel Paksi Aditya](https://www.linkedin.com/in/farrel-paksi-aditya/)

---

## 🙏 Acknowledgments

Terima kasih kepada:
- **Digital Marketing Community Indonesia** untuk insights dan best practices
- **Streamlit & Plotly Community** untuk powerful open-source tools

---

## Resources & References

### **Industry Benchmarks**
- Meta Ads Average CTR (E-commerce): 2-3%
- Profitable ROAS Threshold: > 1.5x
- Industry Standard Conversion Rate: 2-5%

### **Tools & Technologies**
- **Python 3.8+** - Data processing & analysis
- **Streamlit** - Interactive dashboard framework
- **Plotly** - Advanced data visualization
- **Pandas & NumPy** - Data manipulation

### **Recommended Reading**
- "Digital Marketing Analytics" by Chuck Hemann
- "Web Analytics 2.0" by Avinash Kaushik
- Meta Blueprint Certification (Performance Marketing)

---

<div align="center">

**Dashboard ini dikembangkan oleh Tim Deep Dive Analytics 🏆**

*Empowering businesses with data-driven advertising optimization*

⭐ Star repository ini jika membantu optimasi kampanye iklan Anda!

---

© 2026 Deep Dive Analytics Team | Independent Project

**[🚀 Try Live Demo](https://digital-advertising-performance-optimization-dashboard.streamlit.app/)**

</div>
