import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# -------------------------------------------------------------
# 1. PAGE SETUP & DESIGN SPECIFICATIONS
# -------------------------------------------------------------
# Look: Background: #fdf1f3, Brand colour: #be185d (Ruby Rose), Button colour: #be185d
# Headline size: 5.2x body (83px at 1440px), Heaviest weight Host Grotesk, Pill buttons (9999px), Round corners (16px)
# Layout: Roomy spacing, Alternate section backgrounds (#fdf1f3 & #f4e8ea), Flat cards, Staged framing
# Hero layout: Split layout (Text + actions BESIDE large staged image/chart + numbers below)
st.set_page_config(
    page_title="Primeor Analytics | Global E-Commerce Intelligence",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1260px !important;
    }
    
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    html, body, [class*="css"] {
        font-family: 'Host Grotesk', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #fdf1f3;
        color: #000000;
    }
    
    .stApp {
        background-color: #fdf1f3;
        color: #000000;
    }
    
    /* Site Header */
    .brand-header-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #ded2d4;
        margin-bottom: 32px;
    }
    .header-logo {
        font-size: 22px;
        font-weight: 900;
        color: #000000;
        letter-spacing: -0.03em;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .header-logo span {
        color: #be185d;
    }
    .header-nav {
        display: flex;
        gap: 32px;
        font-weight: 600;
        font-size: 14.5px;
        color: #373737;
        align-items: center;
    }
    .header-nav a {
        color: #373737;
        text-decoration: none;
        transition: color 0.15s ease;
    }
    .header-nav a:hover {
        color: #be185d;
    }
    .pill-btn-primary {
        background-color: #be185d;
        color: #fcfcfd !important;
        padding: 10px 24px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 14px;
        text-decoration: none !important;
        display: inline-block;
        border: none;
        box-shadow: 0 4px 14px rgba(190, 24, 93, 0.25);
        transition: all 0.2s ease;
    }
    .pill-btn-primary:hover {
        background-color: #9d174d;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(190, 24, 93, 0.35);
    }
    .pill-btn-secondary {
        background-color: transparent;
        color: #000000;
        padding: 10px 22px;
        border-radius: 9999px;
        font-weight: 700;
        font-size: 14px;
        border: 1.5px solid #ded2d4;
        display: inline-block;
        transition: all 0.2s ease;
    }
    .pill-btn-secondary:hover {
        border-color: #be185d;
        color: #be185d;
    }
    
    /* Split Hero Section on Alternate Ground (#f4e8ea) */
    .hero-split-wrap {
        background-color: #f4e8ea;
        border: 1px solid #ded2d4;
        border-radius: 20px;
        padding: 48px 40px;
        margin-bottom: 36px;
    }
    .hero-h1-huge {
        font-size: 68px;
        font-weight: 900;
        line-height: 1.05;
        letter-spacing: -0.04em;
        color: #000000;
        margin-bottom: 20px;
    }
    .hero-h1-huge span {
        color: #be185d;
    }
    .hero-lead-text {
        font-size: 18px;
        line-height: 1.55;
        color: #373737;
        margin-bottom: 28px;
        max-width: 540px;
    }
    .hero-trust-tag {
        font-size: 13px;
        font-weight: 700;
        color: #be185d;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 12px;
        display: block;
    }
    .hero-terminal-pill {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: #ffffff;
        border: 1px solid #ded2d4;
        border-radius: 9999px;
        padding: 8px 20px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12.5px;
        color: #000000;
        margin-top: 18px;
    }
    
    /* Staged 3D Frame for Product Visual */
    .staged-product-card {
        background: #ffffff;
        border: 1px solid #ded2d4;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 20px 40px -15px rgba(190, 24, 93, 0.12), 0 10px 25px -5px rgba(0, 0, 0, 0.06);
    }
    .card-header-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #fdf1f3;
        border: 1px solid #fbcfe8;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11.5px;
        font-weight: 800;
        color: #be185d;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 8px;
    }
    .pulse-dot {
        width: 7px;
        height: 7px;
        background: #be185d;
        border-radius: 50%;
        display: inline-block;
    }
    
    /* Key Numbers Row (Under Text) */
    .key-metrics-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 36px;
        padding-top: 28px;
        border-top: 1px solid #ded2d4;
    }
    .key-metric-box {
        background: #ffffff;
        border: 1px solid #ded2d4;
        border-radius: 14px;
        padding: 16px 18px;
    }
    .metric-top-label {
        font-size: 11.5px;
        font-weight: 700;
        color: #50504f;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 4px;
    }
    .metric-huge-num {
        font-size: 30px;
        font-weight: 900;
        color: #000000;
        line-height: 1.1;
    }
    .metric-sub-note {
        font-size: 11.5px;
        color: #be185d;
        font-weight: 700;
        margin-top: 4px;
    }
    
    /* Section Headers */
    .sec-heading-main {
        font-size: 38px;
        font-weight: 900;
        color: #000000;
        letter-spacing: -0.025em;
        margin-bottom: 8px;
    }
    .sec-sub-caption {
        font-size: 16px;
        color: #50504f;
        margin-bottom: 28px;
    }
    
    /* Alternate Ground Section Wrapper */
    .section-alt-block {
        background-color: #f4e8ea;
        border: 1px solid #ded2d4;
        border-radius: 20px;
        padding: 48px 36px;
        margin: 44px 0;
    }
    
    /* Comparison Matrix */
    .comp-flat-card {
        background: #ffffff;
        border: 1px solid #ded2d4;
        border-radius: 16px;
        padding: 28px;
        height: 100%;
    }
    .comp-flat-card.highlight {
        border: 2px solid #be185d;
        background: #fffbfa;
    }
    .comp-badge-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    .comp-row {
        display: flex;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px solid #ded2d4;
        font-size: 14px;
        color: #373737;
    }
    .comp-row:last-child {
        border-bottom: none;
    }
    
    /* Logo Cloud Grid */
    .logo-market-tile {
        background: #ffffff;
        border: 1px solid #ded2d4;
        border-radius: 14px;
        padding: 16px 12px;
        text-align: center;
        font-weight: 800;
        color: #000000;
        font-size: 14px;
    }
    
    /* Footer */
    .rose-footer {
        border-top: 1px solid #ded2d4;
        padding: 48px 0 24px 0;
        margin-top: 56px;
        color: #50504f;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 2. DATA LOAD & CACHE
# -------------------------------------------------------------
@st.cache_data
def get_data():
    csv_p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../dataset/cleaned/cleaned_ecommerce_dataset.csv"))
    data = pd.read_csv(csv_p)
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['year_month'] = data['order_date'].dt.to_period('M').astype(str)
    return data

df = get_data()

# -------------------------------------------------------------
# SECTION 1: SITE HEADER
# -------------------------------------------------------------
st.markdown("""
<div class="brand-header-box">
    <div class="header-logo">🌸 Primeor<span>Intelligence</span></div>
    <div class="header-nav">
        <a href="#kpi-focus">Key Numbers</a>
        <a href="#category-comparison">Comparison</a>
        <a href="#market-cloud">Global Markets</a>
        <a href="#visual-features">Visual Trends</a>
        <a href="https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship" target="_blank" class="pill-btn-primary">GitHub Repo ↗</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 2: HERO (Split Layout on Alternate Ground #f4e8ea)
# -------------------------------------------------------------
h_col1, h_col2 = st.columns([1.15, 1])

with h_col1:
    st.markdown("""
    <div style="padding-right: 20px;">
        <span class="hero-trust-tag">✦ Primeor Solutions • 51,271 Audited Records</span>
        <h1 class="hero-h1-huge">Enterprise <span>Sales Data</span> Decoded.</h1>
        <p class="hero-lead-text">
            Autonomous business intelligence across 7 international markets, 13 geographic regions, and 4 shipping classes. Clean Excel ETL, SQLite models, and interactive Power BI decision dashboards.
        </p>
        <div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap;">
            <a href="https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship" target="_blank" class="pill-btn-primary">Explore Repository ➔</a>
            <a href="#visual-features" class="pill-btn-secondary">View Visual Analytics</a>
        </div>
        <div>
            <span class="hero-terminal-pill"><code>pip install pandas plotly streamlit openpyxl reportlab sqlite3</code></span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with h_col2:
    # Staged Interactive Overview Chart (Market Sales Distribution)
    mkt_summary = df.groupby('market')['sales'].sum().reset_index().sort_values('sales', ascending=True)
    fig_hero = px.bar(
        mkt_summary,
        x='sales',
        y='market',
        orientation='h',
        color='sales',
        color_continuous_scale=['#fbcfe8', '#be185d'],
        text_auto='.2s'
    )
    fig_hero.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        coloraxis_showscale=False,
        font=dict(family='Host Grotesk', color='#000000', size=12),
        margin=dict(l=10, r=20, t=10, b=10),
        xaxis=dict(gridcolor='#f4e8ea', showticklabels=False),
        yaxis=dict(gridcolor='#f4e8ea')
    )
    st.markdown("""
    <div class="staged-product-card">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <div class="card-header-badge">
                <span class="pulse-dot"></span>
                <span>Live Intelligence Feed</span>
            </div>
            <span style="font-size:12px; font-weight:700; color:#50504f;">51,271 Records</span>
        </div>
        <div style="font-size:18px; font-weight:900; color:#000000; letter-spacing:-0.02em; margin-bottom:4px;">
            Global Market Revenue Share ($)
        </div>
        <div style="font-size:12.5px; color:#50504f; line-height:1.4; margin-bottom:12px;">
            APAC and Europe account for over 51.6% of enterprise sales across 7 global regions.
        </div>
    """, unsafe_allow_html=True)
    st.plotly_chart(fig_hero, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Key Numbers Row (Under Text)
t_sales = df['sales'].sum()
t_profit = df['profit'].sum()
t_orders = df['order_id'].nunique()
t_discount = df['discount'].mean() * 100
margin = (t_profit / t_sales * 100)

st.markdown(f"""
<div class="key-metrics-grid" id="kpi-focus">
    <div class="key-metric-box">
        <div class="metric-top-label">Gross Revenue</div>
        <div class="metric-huge-num">${t_sales/1e6:.2f}M</div>
        <div class="metric-sub-note">↑ $12,635,222.00 Validated</div>
    </div>
    <div class="key-metric-box">
        <div class="metric-top-label">Net Profit Margin</div>
        <div class="metric-huge-num">${t_profit/1e6:.2f}M</div>
        <div class="metric-sub-note">{margin:.1f}% Enterprise Margin</div>
    </div>
    <div class="key-metric-box">
        <div class="metric-top-label">Total Transactions</div>
        <div class="metric-huge-num">{t_orders:,}</div>
        <div class="metric-sub-note">0 Nulls • Deduplicated</div>
    </div>
    <div class="key-metric-box">
        <div class="metric-top-label">Average Discount</div>
        <div class="metric-huge-num">{t_discount:.2f}%</div>
        <div class="metric-sub-note">Catalog Average Baseline</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# DYNAMIC FILTER SLICERS (Clean Pill Style)
# -------------------------------------------------------------
st.markdown("<p style='color: #be185d; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;'>⚡ INTERACTIVE SLICERS</p>", unsafe_allow_html=True)
fc1, fc2, fc3 = st.columns(3)
with fc1:
    sel_market = st.multiselect("Filter Global Markets:", sorted(df['market'].unique()), default=sorted(df['market'].unique()))
with fc2:
    sel_year = st.multiselect("Filter Calendar Years:", sorted(df['year'].unique()), default=sorted(df['year'].unique()))
with fc3:
    sel_cat = st.multiselect("Filter Product Categories:", sorted(df['category'].unique()), default=sorted(df['category'].unique()))

filtered_df = df[
    (df['market'].isin(sel_market)) &
    (df['year'].isin(sel_year)) &
    (df['category'].isin(sel_cat))
]

if filtered_df.empty:
    st.warning("No records found for current filter selections. Please broaden your selection.")
    st.stop()

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 3: COMPARISON (2 PRODUCTS / CATEGORIES)
# -------------------------------------------------------------
st.markdown("<h2 class='sec-heading-main' id='category-comparison'>Category Performance Comparison</h2>", unsafe_allow_html=True)
st.markdown("<p class='sec-sub-caption'>Direct operational comparison between high-margin Technology drivers and margin-diluting Furniture assortments.</p>", unsafe_allow_html=True)

cp1, cp2 = st.columns(2)
with cp1:
    st.markdown("""
    <div class="comp-flat-card highlight">
        <span class="comp-badge-pill" style="background:#fce7f3; color:#be185d;">HIGH-PERFORMANCE PILLAR</span>
        <h3 style="font-size:20px; font-weight:800; color:#000000; margin-bottom:14px;">Technology Category (Core Profit Engine)</h3>
        <div class="comp-row"><span>Gross Sales Volume</span><strong>$4,742,975.00</strong></div>
        <div class="comp-row"><span>Cumulative Net Profit</span><strong style="color: #be185d;">$663,337.29</strong></div>
        <div class="comp-row"><span>Net Operating Margin</span><strong>13.98%</strong></div>
        <div class="comp-row"><span>Average Profit per Order</span><strong>$65.44 / order</strong></div>
        <div class="comp-row"><span>Average Discount Applied</span><strong>13.54% (Disciplined)</strong></div>
        <div class="comp-row"><span>Top Profit Driver</span><strong>Canon imageCLASS Copier ($25.2k)</strong></div>
        <p style="margin-top: 14px; font-size: 13px; color: #50504f;">Strategic Assessment: Top revenue and cash flow provider with strong warranty buffers.</p>
    </div>
    """, unsafe_allow_html=True)

with cp2:
    st.markdown("""
    <div class="comp-flat-card">
        <span class="comp-badge-pill" style="background:#f4e8ea; color:#50504f;">MARGIN DILUTION HAZARD</span>
        <h3 style="font-size:20px; font-weight:800; color:#000000; margin-bottom:14px;">Furniture Category (Discount Dilution)</h3>
        <div class="comp-row"><span>Gross Sales Volume</span><strong>$4,105,771.00</strong></div>
        <div class="comp-row"><span>Cumulative Net Profit</span><strong>$286,164.92</strong></div>
        <div class="comp-row"><span>Net Operating Margin</span><strong style="color: #be185d;">6.97% (50% Below Tech)</strong></div>
        <div class="comp-row"><span>Average Profit per Order</span><strong>$29.00 / order</strong></div>
        <div class="comp-row"><span>Average Discount Applied</span><strong style="color: #be185d;">16.80% (Highest Across Catalog)</strong></div>
        <div class="comp-row"><span>Severe Negative Loss Line</span><strong style="color: #be185d;">Tables (-$64,113.55 Loss)</strong></div>
        <p style="margin-top: 14px; font-size: 13px; color: #50504f;">Strategic Recommendation: Enforce strict 15% discount caps on bulky freight tables.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 4: LOGO CLOUD (On Alternate Ground #f4e8ea)
# -------------------------------------------------------------
st.markdown("""
<div class="section-alt-block" id="market-cloud">
    <h2 class='sec-heading-main' style='text-align: center;'>Global Geographic Footprint</h2>
    <p class='sec-sub-caption' style='text-align: center; max-width: 650px; margin: 0 auto 32px auto;'>
        Revenue concentration mapped across the 6 primary international commercial market clusters.
    </p>
""", unsafe_allow_html=True)

l1, l2, l3, l4, l5, l6 = st.columns(6)
mkt_shares = filtered_df.groupby('market')['sales'].sum()
with l1: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>ASIA-PACIFIC</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>APAC</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('APAC', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)
with l2: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>EUROPEAN UNION</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>EU</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('EU', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)
with l3: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>UNITED STATES</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>US</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('US', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)
with l4: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>LATIN AMERICA</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>LATAM</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('LATAM', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)
with l5: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>MID-EAST / AFRICA</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>EMEA</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('EMEA', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)
with l6: st.markdown(f"<div class='logo-market-tile'><div style='font-size:11px; color:#50504f; font-weight:700;'>AFRICA REGION</div><div style='font-size:16px; font-weight:900; color:#000000; margin:3px 0;'>Africa</div><span style='color: #be185d; font-size: 13.5px; font-weight:800;'>${mkt_shares.get('Africa', 0)/1e6:.2f}M</span></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 5: FEATURES (Swapping Chart and Text Rows)
# -------------------------------------------------------------
st.markdown("<h2 class='sec-heading-main' id='visual-features'>Interactive Analytical Features</h2>", unsafe_allow_html=True)
st.markdown("<p class='sec-sub-caption'>Granular time-series trends, geographic distribution, and sub-category profitability diagnostics.</p>", unsafe_allow_html=True)

# Row 1: Chart Left, Text Right
r1_c1, r1_c2 = st.columns([1.5, 1])
with r1_c1:
    mkt_summary2 = filtered_df.groupby('market').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values('sales', ascending=True)
    fig1 = px.bar(
        mkt_summary2,
        x='sales',
        y='market',
        orientation='h',
        color='sales',
        color_continuous_scale=['#fce7f3', '#be185d'],
        text_auto='.2s'
    )
    fig1.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        coloraxis_showscale=False,
        font=dict(family='Host Grotesk', color='#000000'),
        margin=dict(l=20, r=20, t=10, b=10),
        xaxis=dict(gridcolor='#f4e8ea'),
        yaxis=dict(gridcolor='#f4e8ea')
    )
    st.markdown('<div class="staged-product-card">', unsafe_allow_html=True)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with r1_c2:
    st.markdown("""
    <div style="padding: 24px 10px;">
        <span style="color: #be185d; font-weight: 800; font-size: 13px; text-transform: uppercase;">01. GEOGRAPHIC EXPANSION</span>
        <h3 style="font-size: 24px; font-weight: 900; margin-top: 6px; color: #000000;">APAC & EU Generate 51.6% of Global Sales</h3>
        <p style="color: #373737; line-height: 1.6; font-size: 15px;">
            The Asia-Pacific territory leads international turnover at $3.58M with $437k in net profits, followed by the European Union at $2.94M. Strategic focus should be on establishing dedicated regional logistics hubs to reduce localized delivery lead-times.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 2: Text Left, Chart Right (Swapped)
r2_c1, r2_c2 = st.columns([1, 1.5])
with r2_c1:
    st.markdown("""
    <div style="padding: 24px 10px;">
        <span style="color: #be185d; font-weight: 800; font-size: 13px; text-transform: uppercase;">02. TIME-SERIES PREDICTABILITY</span>
        <h3 style="font-size: 24px; font-weight: 900; margin-top: 6px; color: #000000;">Empirical Q4 Seasonality Surge (Sept - Dec)</h3>
        <p style="color: #373737; line-height: 1.6; font-size: 15px;">
            Monthly sales trend mapping across 48 continuous months proves that global transactions spike 2.5x from September through December, exceeding $400k+/month. Inventory replenishment and freight carrier contracts must be pre-arranged by late summer.
        </p>
    </div>
    """, unsafe_allow_html=True)
with r2_c2:
    trend_df = filtered_df.groupby('year_month')['sales'].sum().reset_index()
    fig2 = px.line(trend_df, x='year_month', y='sales', line_shape='spline')
    fig2.update_traces(line_color='#be185d', line_width=3)
    fig2.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font=dict(family='Host Grotesk', color='#000000'),
        margin=dict(l=20, r=20, t=10, b=10),
        xaxis=dict(gridcolor='#f4e8ea', title="Order Year-Month"),
        yaxis=dict(gridcolor='#f4e8ea', title="Sales Revenue ($)")
    )
    st.markdown('<div class="staged-product-card">', unsafe_allow_html=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 3: Chart Left, Text Right (Swapped)
r3_c1, r3_c2 = st.columns([1.5, 1])
with r3_c1:
    sub_df = filtered_df.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=True)
    sub_df['bar_color'] = sub_df['profit'].apply(lambda x: '#be185d' if x < 0 else '#000000')
    fig3 = go.Figure(go.Bar(
        x=sub_df['profit'],
        y=sub_df['sub_category'],
        orientation='h',
        marker_color=sub_df['bar_color'],
        text=[f"${v:,.0f}" for v in sub_df['profit']],
        textposition='outside'
    ))
    fig3.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font=dict(family='Host Grotesk', color='#000000'),
        margin=dict(l=20, r=20, t=10, b=10),
        xaxis=dict(gridcolor='#f4e8ea', title="Profit / Loss ($)"),
        yaxis=dict(gridcolor='#f4e8ea')
    )
    st.markdown('<div class="staged-product-card">', unsafe_allow_html=True)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with r3_c2:
    st.markdown("""
    <div style="padding: 24px 10px;">
        <span style="color: #be185d; font-weight: 800; font-size: 13px; text-transform: uppercase;">03. UNRESTRAINED DISCOUNT RISKS</span>
        <h3 style="font-size: 24px; font-weight: 900; margin-top: 6px; color: #000000;">Stopping the -$64,113 Loss in Tables</h3>
        <p style="color: #373737; line-height: 1.6; font-size: 15px;">
            While Copiers ($258k profit) and Phones ($217k profit) generate sustainable cash flow, Tables produced severe negative net profit (-$64k). Root cause auditing isolated heavy discount rates (>35%) coupled with high freight charges.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 6: DOWNLOAD (On Alternate Ground #f4e8ea)
# -------------------------------------------------------------
st.markdown("""
<div class="section-alt-block">
    <h2 class='sec-heading-main'>Download Project Artifacts</h2>
    <p class='sec-sub-caption'>Command-line ingestion and native project templates for Power BI, Excel, and SQL engines.</p>
""", unsafe_allow_html=True)

d1, d2 = st.columns([1.4, 1])
with d1:
    st.markdown("""
    <div class="comp-flat-card">
        <div style="font-size: 12px; color: #be185d; font-weight: 800; margin-bottom: 8px;">TERMINAL INSTALLATION & SETUP COMMAND</div>
        <div style="background-color: #fdf1f3; padding: 14px 18px; border-radius: 10px; font-family: 'JetBrains Mono', monospace; font-size: 14px; border: 1px solid #ded2d4; color: #000000;">
            pip install pandas plotly streamlit openpyxl reportlab sqlite3
        </div>
        <p style="margin-top: 12px; font-size: 13px; color: #50504f;">Runs locally on Windows, macOS, and Linux servers.</p>
    </div>
    """, unsafe_allow_html=True)
with d2:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 10px;">
        <div class="logo-market-tile" style="text-align: left; padding: 14px 20px;">💾 <b>Power BI (.pbix & .pbit)</b> — 3-Page Executive Model</div>
        <div class="logo-market-tile" style="text-align: left; padding: 14px 20px;">📊 <b>Excel Model (.xlsx)</b> — Formula KPIs & Embedded Charts</div>
        <div class="logo-market-tile" style="text-align: left; padding: 14px 20px;">📑 <b>Executive PDF (.pdf)</b> — Formal Leadership Report</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 7: BLOG / MILESTONE INDEX
# -------------------------------------------------------------
st.markdown("<h2 class='sec-heading-main'>Internship Technical Progression</h2>", unsafe_allow_html=True)
st.markdown("<p class='sec-sub-caption'>Documented completion of all required project levels under the Primeor Solutions program.</p>", unsafe_allow_html=True)

b_feat, b_short = st.columns([1.4, 1])
with b_feat:
    st.markdown("""
    <div class="comp-flat-card" style="border: 2px solid #be185d;">
        <span style="color: #be185d; font-weight: 800; font-size: 12px; text-transform: uppercase;">✦ FEATURED MILESTONE • LEVEL 3</span>
        <h3 style="font-size: 24px; font-weight: 900; margin: 10px 0; color: #000000;">Interactive Power BI Executive Dashboard & UI Overhaul</h3>
        <p style="color: #373737; font-size: 15px; line-height: 1.6;">
            Architecting a 3-page interactive decision support dashboard featuring synchronized multi-market slicers, DAX time-intelligence models, and deep-dive loss order diagnostics across 51,271 global transactions.
        </p>
        <div style="margin-top: 16px; font-size: 13px; color: #be185d; font-weight: 700;">Author: Rishi Prajapati &nbsp;|&nbsp; Status: 100% Completed & Verified</div>
    </div>
    """, unsafe_allow_html=True)

with b_short:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 14px;">
        <div class="comp-flat-card" style="padding: 16px 20px;">
            <span style="color: #be185d; font-weight: 800; font-size: 11px;">LEVEL 1 COMPLETED</span>
            <div style="font-size: 15px; font-weight: 800; color: #000000;">Excel Data Understanding & Cleaning</div>
            <div style="font-size: 12px; color: #50504f;">Deduplication, 0 Nulls Remaining, Pivot Tables & Visuals</div>
        </div>
        <div class="comp-flat-card" style="padding: 16px 20px;">
            <span style="color: #be185d; font-weight: 800; font-size: 11px;">LEVEL 2 COMPLETED</span>
            <div style="font-size: 15px; font-weight: 800; color: #000000;">SQL Data Analysis & Relational Engine</div>
            <div style="font-size: 12px; color: #50504f;">10 Core Business Queries, Multi-Sheet Workbook, SQLite Database</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 8: CLOSING PANEL (On Alternate Ground #f4e8ea)
# -------------------------------------------------------------
st.markdown("""
<div class="section-alt-block" style="text-align: center; padding: 56px 36px;">
    <h2 style="font-size: 38px; font-weight: 900; color: #000000; margin-bottom: 12px; letter-spacing: -0.03em;">Inspect the Production Repository</h2>
    <p style="font-size: 16px; color: #373737; max-width: 650px; margin: 0 auto 28px auto; line-height: 1.6;">
        Explore all verified data cleaning scripts, SQLite database models, SQL queries, and Power BI deliverables on GitHub.
    </p>
    <div>
        <a href="https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship" target="_blank" class="pill-btn-primary" style="padding: 14px 38px; font-size: 15px;">Open GitHub Repository ➔</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 9: FOOTER
# -------------------------------------------------------------
st.markdown("""
<div class="rose-footer">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 24px;">
        <div>
            <div style="font-weight: 900; color: #000000; font-size: 17px; margin-bottom: 6px;">🌸 Primeor Solutions Internship Project</div>
            <p style="max-width: 340px; color: #50504f; font-size: 13px; line-height: 1.5;">Empirical business intelligence bridging transactional data and executive strategy.</p>
        </div>
        <div style="display: flex; gap: 50px;">
            <div>
                <b style="color: #000000;">Project Deliverables</b><br>
                Level 1: Excel Workbook<br>
                Level 2: SQL Scripts & SQLite<br>
                Level 3: Power BI (.pbix)
            </div>
            <div>
                <b style="color: #000000;">Author Information</b><br>
                Rishi Prajapati<br>
                Data Analytics Intern<br>
                Primeor Solutions
            </div>
        </div>
    </div>
    <div style="text-align: center; margin-top: 36px; font-size: 12px; color: #50504f;">
        © 2026 Primeor Solutions Data Analytics Internship. Confidential & Verified.
    </div>
</div>
""", unsafe_allow_html=True)
