import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# -------------------------------------------------------------
# 1. PAGE SETUP & DESIGN SPECIFICATIONS
# -------------------------------------------------------------
# Host Grotesk font, #ffffff page ground, #2e5bff accent, soft corners (8px), pill controls (9999px)
st.set_page_config(
    page_title="Primeor Analytics | Global E-Commerce Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject Clean SaaS Landing Page CSS according to <look> & <starting-values>
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Host Grotesk', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #ffffff;
        color: #201f20;
    }
    
    .stApp {
        background-color: #ffffff;
        color: #201f20;
    }
    
    /* Clean Site Header */
    .site-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 24px;
        border-bottom: 1px solid #e0e0df;
        background-color: #ffffff;
        margin-bottom: 32px;
    }
    .brand-logo {
        font-size: 20px;
        font-weight: 700;
        color: #201f20;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .brand-logo span {
        color: #2e5bff;
    }
    
    /* Hero Section */
    .hero-container {
        max-width: 1100px;
        margin: 0 auto 40px auto;
        text-align: center;
        padding: 40px 16px 20px 16px;
    }
    .hero-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 9999px;
        background-color: #f7f6f6;
        border: 1px solid #e0e0df;
        font-size: 13px;
        font-weight: 600;
        color: #2e5bff;
        margin-bottom: 20px;
    }
    .hero-title {
        font-size: 48px;
        font-weight: 700;
        line-height: 1.15;
        color: #201f20;
        margin-bottom: 18px;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 18px;
        line-height: 1.6;
        color: #494949;
        max-width: 760px;
        margin: 0 auto 28px auto;
    }
    .code-pill {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background-color: #f7f6f6;
        border: 1px solid #e0e0df;
        border-radius: 9999px;
        padding: 8px 22px;
        font-family: monospace;
        font-size: 14px;
        color: #201f20;
        margin-top: 14px;
    }
    
    /* Metric Cards */
    .kpi-card {
        background-color: #f7f6f6;
        border: 1px solid #e0e0df;
        border-radius: 8px;
        padding: 24px;
        text-align: left;
        transition: transform 0.15s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
    }
    .kpi-label {
        font-size: 13px;
        font-weight: 600;
        color: #606060;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 8px;
    }
    .kpi-number {
        font-size: 32px;
        font-weight: 700;
        color: #201f20;
        line-height: 1.1;
        margin-bottom: 4px;
    }
    .kpi-sub {
        font-size: 12px;
        color: #2e5bff;
        font-weight: 600;
    }
    
    /* Section Headings */
    .section-title {
        font-size: 30px;
        font-weight: 700;
        color: #201f20;
        letter-spacing: -0.01em;
        margin-bottom: 8px;
    }
    .section-desc {
        font-size: 15px;
        color: #606060;
        margin-bottom: 24px;
    }
    
    /* Comparison Matrix */
    .comp-box {
        background-color: #ffffff;
        border: 1px solid #e0e0df;
        border-radius: 8px;
        padding: 24px;
        height: 100%;
    }
    .comp-box.highlight {
        border: 2px solid #2e5bff;
        background-color: #fcfdfe;
    }
    .comp-title {
        font-size: 18px;
        font-weight: 700;
        color: #201f20;
        margin-bottom: 16px;
    }
    .comp-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px solid #e0e0df;
        font-size: 14px;
    }
    .comp-row:last-child {
        border-bottom: none;
    }
    
    /* Logo Cloud */
    .logo-badge {
        background-color: #f7f6f6;
        border: 1px solid #e0e0df;
        border-radius: 8px;
        padding: 14px;
        text-align: center;
        font-weight: 600;
        color: #494949;
        font-size: 13px;
    }
    
    /* Closing Card */
    .closing-banner {
        background-color: #141314;
        color: #fcfcfd;
        border-radius: 12px;
        padding: 56px 40px;
        text-align: center;
        margin: 50px 0 30px 0;
    }
    .closing-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #fcfcfd;
    }
    .closing-desc {
        font-size: 16px;
        color: #a0a0a0;
        max-width: 600px;
        margin: 0 auto 24px auto;
    }
    
    /* Footer */
    .site-footer {
        border-top: 1px solid #e0e0df;
        padding: 40px 0 20px 0;
        margin-top: 40px;
        color: #606060;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 2. DATA LOAD & CACHING
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
<div class="site-header">
    <div class="brand-logo">⚡ Primeor<span>Analytics</span></div>
    <div style="display:flex; gap: 24px; font-weight: 500; font-size: 14px; color: #494949; align-items: center;">
        <span>Platform</span>
        <span>Global Analytics</span>
        <span>SQL Models</span>
        <span>Documentation</span>
        <span style="background-color: #2e5bff; color: #ffffff; padding: 6px 18px; border-radius: 9999px; font-weight: 600; cursor: pointer;">Internship Portal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 2: HERO
# -------------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">Enterprise Data Intelligence • 51,271 Records</div>
    <h1 class="hero-title">Turn Global E-Commerce Data into High-Margin Decisions</h1>
    <p class="hero-subtitle">
        Empirical business intelligence across 7 international markets, 13 geographic regions, and 4 shipping modes. Built with Python, SQLite, Excel, and Power BI.
    </p>
    <div>
        <span class="code-pill"><code>git clone https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship.git</code></span>
    </div>
</div>
""", unsafe_allow_html=True)

# Live Filter Controls in clean pill layout
st.markdown("<p style='text-align: center; color: #606060; font-size: 14px; font-weight: 600; margin-bottom: 10px;'>FILTER REAL-TIME DASHBOARD DATA</p>", unsafe_allow_html=True)
fc1, fc2, fc3 = st.columns(3)
with fc1:
    sel_market = st.multiselect("Select Markets:", sorted(df['market'].unique()), default=sorted(df['market'].unique()))
with fc2:
    sel_year = st.multiselect("Select Years:", sorted(df['year'].unique()), default=sorted(df['year'].unique()))
with fc3:
    sel_cat = st.multiselect("Select Categories:", sorted(df['category'].unique()), default=sorted(df['category'].unique()))

filtered_df = df[
    (df['market'].isin(sel_market)) &
    (df['year'].isin(sel_year)) &
    (df['category'].isin(sel_cat))
]

if filtered_df.empty:
    st.warning("No records found for current filter. Please broaden selection.")
    st.stop()

# 4 Key Starting Numbers (KPI Cards)
t_sales = filtered_df['sales'].sum()
t_profit = filtered_df['profit'].sum()
t_orders = filtered_df['order_id'].nunique()
t_discount = filtered_df['discount'].mean() * 100
margin = (t_profit / t_sales * 100) if t_sales else 0

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Revenue</div>
        <div class="kpi-number">${t_sales:,.0f}</div>
        <div class="kpi-sub">↑ Global Gross Sales</div>
    </div>
    """, unsafe_allow_html=True)
with k2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Net Profit</div>
        <div class="kpi-number">${t_profit:,.0f}</div>
        <div class="kpi-sub" style="color: #06D6A0;">{margin:.1f}% Profit Margin</div>
    </div>
    """, unsafe_allow_html=True)
with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Orders</div>
        <div class="kpi-number">{t_orders:,}</div>
        <div class="kpi-sub">Fulfillment Transactions</div>
    </div>
    """, unsafe_allow_html=True)
with k4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Average Discount</div>
        <div class="kpi-number">{t_discount:.2f}%</div>
        <div class="kpi-sub" style="color: #ef476f;">Across Product Assortment</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 3: COMPARISON (2 PRODUCTS / STRATEGIES)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>Enterprise Analytics Comparison</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-desc'>Evaluating core category margin contributions and risk profiles across 6 operational dimensions.</p>", unsafe_allow_html=True)

cp1, cp2 = st.columns(2)
with cp1:
    st.markdown("""
    <div class="comp-box highlight">
        <div class="comp-title">⭐ Technology Category (Core Driver)</div>
        <div class="comp-row"><span>Gross Sales Revenue</span><strong>$4,742,975.00</strong></div>
        <div class="comp-row"><span>Cumulative Net Profit</span><strong style="color: #06D6A0;">$663,337.29</strong></div>
        <div class="comp-row"><span>Net Profit Margin</span><strong>13.98%</strong></div>
        <div class="comp-row"><span>Average Order Profit</span><strong>$65.44 / order</strong></div>
        <div class="comp-row"><span>Discount Exposure</span><strong>13.54% (Controlled)</strong></div>
        <div class="comp-row"><span>Top Product Offering</span><strong>Canon imageCLASS Copier</strong></div>
        <p style="margin-top: 14px; font-size: 12px; color: #606060;">Recommendation: Expand distribution and protect warranty margin tier.</p>
    </div>
    """, unsafe_allow_html=True)

with cp2:
    st.markdown("""
    <div class="comp-box">
        <div class="comp-title">⚠️ Furniture Category (Margin Drag)</div>
        <div class="comp-row"><span>Gross Sales Revenue</span><strong>$4,105,771.00</strong></div>
        <div class="comp-row"><span>Cumulative Net Profit</span><strong style="color: #ef476f;">$286,164.92</strong></div>
        <div class="comp-row"><span>Net Profit Margin</span><strong>6.97% (Severe Lag)</strong></div>
        <div class="comp-row"><span>Average Order Profit</span><strong>$29.00 / order</strong></div>
        <div class="comp-row"><span>Discount Exposure</span><strong style="color: #ef476f;">16.80% (Highest)</strong></div>
        <div class="comp-row"><span>Critical Loss Sub-Category</span><strong style="color: #ef476f;">Tables (-$64,113.55)</strong></div>
        <p style="margin-top: 14px; font-size: 12px; color: #606060;">Recommendation: Enforce 15% discount caps on bulky freight furniture.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 4: LOGO CLOUD (6 GLOBAL MARKETS GRID)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>Global Market Penetration</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-desc'>Transaction distribution across the 6 major enterprise geographic territories.</p>", unsafe_allow_html=True)

l1, l2, l3, l4, l5, l6 = st.columns(6)
mkt_shares = filtered_df.groupby('market')['sales'].sum()
with l1: st.markdown(f"<div class='logo-badge'>🌏 APAC<br><small>${mkt_shares.get('APAC', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)
with l2: st.markdown(f"<div class='logo-badge'>🇪🇺 EU<br><small>${mkt_shares.get('EU', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)
with l3: st.markdown(f"<div class='logo-badge'>🇺🇸 US<br><small>${mkt_shares.get('US', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)
with l4: st.markdown(f"<div class='logo-badge'>🌎 LATAM<br><small>${mkt_shares.get('LATAM', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)
with l5: st.markdown(f"<div class='logo-badge'>🌍 EMEA<br><small>${mkt_shares.get('EMEA', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)
with l6: st.markdown(f"<div class='logo-badge'>🇿🇦 Africa<br><small>${mkt_shares.get('Africa', 0)/1e6:.2f}M</small></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 5: FEATURES (3 INTERACTIVE VISUAL ROWS SWAPPING SIDES)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>Interactive Analytical Features</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-desc'>In-depth empirical charts exploring regional volume, fulfillment cadence, and product level risks.</p>", unsafe_allow_html=True)

# Row 1: Image/Chart Left, Text Right
r1_c1, r1_c2 = st.columns([1.4, 1])
with r1_c1:
    mkt_summary = filtered_df.groupby('market').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values('sales', ascending=True)
    fig1 = px.bar(
        mkt_summary,
        x='sales',
        y='market',
        orientation='h',
        color='sales',
        color_continuous_scale=['#f7f6f6', '#2e5bff'],
        text_auto='.2s'
    )
    fig1.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#f7f6f6',
        coloraxis_showscale=False,
        font=dict(family='Host Grotesk', color='#201f20'),
        margin=dict(l=20, r=20, t=10, b=10)
    )
    st.plotly_chart(fig1, use_container_width=True)
with r1_c2:
    st.markdown("""
    <div style="padding-top: 20px;">
        <span style="color: #2e5bff; font-weight: 700; font-size: 13px;">01. GEOGRAPHIC EXPANSION</span>
        <h3 style="font-size: 22px; font-weight: 700; margin-top: 4px;">APAC & Europe Generate 51.6% of Global Sales</h3>
        <p style="color: #494949; line-height: 1.6; font-size: 14px;">
            The Asia-Pacific territory leads international turnover at $3.58M with $437k in net profits, followed by the European Union at $2.94M. Strategic focus should be on establishing dedicated regional logistics hubs to reduce localized delivery lead-times.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 2: Text Left, Chart Right (Swap Sides)
r2_c1, r2_c2 = st.columns([1, 1.4])
with r2_c1:
    st.markdown("""
    <div style="padding-top: 20px;">
        <span style="color: #2e5bff; font-weight: 700; font-size: 13px;">02. TIME-SERIES INTELLIGENCE</span>
        <h3 style="font-size: 22px; font-weight: 700; margin-top: 4px;">Predictable Q4 Peak Surges Every Year</h3>
        <p style="color: #494949; line-height: 1.6; font-size: 14px;">
            Monthly sales trend mapping across 48 months proves that global transactions spike 2.5x from September through December, exceeding $400k+/month. Inventory replenishment and freight carrier contracts must be pre-arranged by late summer.
        </p>
    </div>
    """, unsafe_allow_html=True)
with r2_c2:
    trend_df = filtered_df.groupby('year_month')['sales'].sum().reset_index()
    fig2 = px.line(trend_df, x='year_month', y='sales', line_shape='spline')
    fig2.update_traces(line_color='#2e5bff', line_width=3)
    fig2.update_layout(
        paper_bgcolor='#ffffff',
        plot_bgcolor='#f7f6f6',
        font=dict(family='Host Grotesk', color='#201f20'),
        margin=dict(l=20, r=20, t=10, b=10),
        xaxis_title="Year-Month",
        yaxis_title="Revenue ($)"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 3: Chart Left, Text Right (Swap Sides)
r3_c1, r3_c2 = st.columns([1.4, 1])
with r3_c1:
    sub_df = filtered_df.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=True)
    sub_df['bar_color'] = sub_df['profit'].apply(lambda x: '#ef476f' if x < 0 else '#2e5bff')
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
        plot_bgcolor='#f7f6f6',
        font=dict(family='Host Grotesk', color='#201f20'),
        margin=dict(l=20, r=20, t=10, b=10)
    )
    st.plotly_chart(fig3, use_container_width=True)
with r3_c2:
    st.markdown("""
    <div style="padding-top: 20px;">
        <span style="color: #ef476f; font-weight: 700; font-size: 13px;">03. MARGIN PROTECTION</span>
        <h3 style="font-size: 22px; font-weight: 700; margin-top: 4px;">Stopping the $64k Loss in Tables</h3>
        <p style="color: #494949; line-height: 1.6; font-size: 14px;">
            While Copiers ($258k profit) and Phones ($217k profit) generate sustainable cash flow, Tables produced severe negative net profit (-$64k). Root cause auditing isolated heavy discount rates (>35%) coupled with high freight charges.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 6: DOWNLOAD (COMMAND + 3 PLATFORMS)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>Download Analytics Project Artifacts</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-desc'>Access production database schemas, Power BI dashboard templates, and automated ETL notebooks.</p>", unsafe_allow_html=True)

d_col1, d_col2 = st.columns([1.4, 1])
with d_col1:
    st.markdown("""
    <div class="comp-box" style="background-color: #f7f6f6;">
        <div style="font-size: 13px; color: #606060; font-weight: 600; margin-bottom: 8px;">TERMINAL INSTALLATION COMMAND</div>
        <div style="font-family: monospace; font-size: 15px; color: #201f20; font-weight: 600;">
            pip install pandas plotly streamlit openpyxl reportlab sqlite3
        </div>
        <p style="margin-top: 10px; font-size: 12px; color: #606060;">Runs locally on Windows, macOS, and Linux servers.</p>
    </div>
    """, unsafe_allow_html=True)
with d_col2:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 10px;">
        <div class="logo-badge" style="text-align: left; padding: 12px 18px;">💾 <b>Power BI (.pbix)</b> — Interactive Template</div>
        <div class="logo-badge" style="text-align: left; padding: 12px 18px;">📊 <b>Excel Model (.xlsx)</b> — Formula KPIs & Pivots</div>
        <div class="logo-badge" style="text-align: left; padding: 12px 18px;">📑 <b>Executive PDF (.pdf)</b> — Formal Leadership Report</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 7: BLOG / MILESTONE INDEX (1 FEATURED + SHORT LIST)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>Internship Project Milestones</h2>", unsafe_allow_html=True)
st.markdown("<p class='section-desc'>Chronological technical progression through the Primeor Solutions data analytics curriculum.</p>", unsafe_allow_html=True)

b_featured, b_list = st.columns([1.3, 1])
with b_featured:
    st.markdown("""
    <div class="comp-box" style="border: 1px solid #e0e0df;">
        <span style="color: #2e5bff; font-weight: 700; font-size: 12px;">FEATURED MILESTONE • LEVEL 3</span>
        <h3 style="font-size: 22px; font-weight: 700; margin: 8px 0;">Interactive Power BI Executive Dashboard & UI Overhaul</h3>
        <p style="color: #494949; font-size: 14px; line-height: 1.6;">
            Constructing a 3-page C-suite dashboard with synchronized multi-dimensional slicers, custom color palettes, and empirical loss-order diagnostics across 51,271 records.
        </p>
        <div style="margin-top: 14px; font-size: 12px; color: #606060;">Author: Rishi Prajapati • Status: 100% Completed</div>
    </div>
    """, unsafe_allow_html=True)

with b_list:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 14px;">
        <div style="border-bottom: 1px solid #e0e0df; padding-bottom: 10px;">
            <span style="color: #06D6A0; font-weight: 700; font-size: 11px;">LEVEL 1 COMPLETED</span>
            <div style="font-size: 15px; font-weight: 600; color: #201f20;">Data Understanding, Deduplication & Pivot Table Models</div>
            <div style="font-size: 12px; color: #606060;">Excel Formulas, Summary KPIs & Embedded Visual Charts</div>
        </div>
        <div>
            <span style="color: #2e5bff; font-weight: 700; font-size: 11px;">LEVEL 2 COMPLETED</span>
            <div style="font-size: 15px; font-weight: 600; color: #201f20;">Relational SQL Database Ingestion & 10 Core Business Queries</div>
            <div style="font-size: 12px; color: #606060;">SQLite Engine, Multi-sheet Excel exports & PDF Report</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 8: CLOSING PANEL
# -------------------------------------------------------------
st.markdown("""
<div class="closing-banner">
    <h2 class="closing-title">Ready to Review the Complete Project Repository?</h2>
    <p class="closing-desc">
        Explore production scripts, clean dataset CSVs, SQL schema definitions, and interactive dashboard packages in one unified GitHub workspace.
    </p>
    <div style="display: flex; justify-content: center; gap: 16px;">
        <a href="https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship" target="_blank" style="text-decoration: none; background-color: #2e5bff; color: #ffffff; padding: 12px 28px; border-radius: 9999px; font-weight: 600; font-size: 14px;">View on GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 9: FOOTER
# -------------------------------------------------------------
st.markdown("""
<div class="site-footer">
    <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div>
            <div style="font-weight: 700; color: #201f20; font-size: 15px; margin-bottom: 6px;">Primeor Solutions Internship Project</div>
            <p style="max-width: 300px; color: #606060; font-size: 12px;">Bridging real-world business analytics and executive decision-making.</p>
        </div>
        <div style="display: flex; gap: 40px;">
            <div>
                <b style="color: #201f20;">Project Levels</b><br>
                Level 1: Excel<br>
                Level 2: SQL Analytics<br>
                Level 3: Power BI
            </div>
            <div>
                <b style="color: #201f20;">Author & Contact</b><br>
                Rishi Prajapati<br>
                Data Analytics Intern<br>
                Primeor Solutions
            </div>
        </div>
    </div>
    <div style="text-align: center; margin-top: 24px; font-size: 12px; color: #8D99AE;">
        © 2026 Primeor Solutions Data Analytics Internship. All deliverables audited and verified.
    </div>
</div>
""", unsafe_allow_html=True)
