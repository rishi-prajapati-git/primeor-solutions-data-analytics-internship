import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import os

# -------------------------------------------------------------
# GLOBAL PALETTE & STYLING
# -------------------------------------------------------------
BG_COLOR = "#0B132B"       # Deep Executive Midnight Navy
CARD_BG = "#1C2541"        # Slate Card Container
TEXT_PRIMARY = "#FFFFFF"   # Pure White
TEXT_MUTED = "#8D99AE"     # Muted Platinum Gray
ACCENT_BLUE = "#3A86FF"    # Radiant Corporate Blue
ACCENT_GREEN = "#06D6A0"   # KPI Emerald Green
ACCENT_ORANGE = "#FFB703"  # Vibrant Amber
ACCENT_RED = "#EF476F"     # Risk Alert Coral Red

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dataset/cleaned/cleaned_ecommerce_dataset.csv'))
df = pd.read_csv(csv_path)
df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M').astype(str)

out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../dashboard_mockups'))
os.makedirs(out_dir, exist_ok=True)

# -------------------------------------------------------------
# PAGE 1: EXECUTIVE OVERVIEW
# -------------------------------------------------------------
def render_page1():
    fig = plt.figure(figsize=(16, 9), facecolor=BG_COLOR)
    gs = gridspec.GridSpec(3, 4, figure=fig, height_ratios=[1.2, 3.5, 3.5], hspace=0.35, wspace=0.25)
    
    # Header Title Banner
    fig.text(0.04, 0.95, "PRIMEOR SOLUTIONS | GLOBAL E-COMMERCE EXECUTIVE DASHBOARD", fontsize=18, fontweight='bold', color=TEXT_PRIMARY)
    fig.text(0.04, 0.92, "Page 1: Executive KPI Overview & Enterprise Performance Summary | Active Filters: All Markets (2011 - 2014)", fontsize=10, color=TEXT_MUTED)
    
    # KPI 1: Total Sales
    ax_kpi1 = fig.add_subplot(gs[0, 0])
    ax_kpi1.set_facecolor(CARD_BG)
    ax_kpi1.text(0.5, 0.65, "TOTAL REVENUE", ha='center', va='center', fontsize=11, fontweight='bold', color=TEXT_MUTED)
    ax_kpi1.text(0.5, 0.30, "$12.64M", ha='center', va='center', fontsize=22, fontweight='bold', color=ACCENT_BLUE)
    ax_kpi1.axis('off')
    for spine in ax_kpi1.spines.values(): spine.set_visible(False)
    
    # KPI 2: Total Profit
    ax_kpi2 = fig.add_subplot(gs[0, 1])
    ax_kpi2.set_facecolor(CARD_BG)
    ax_kpi2.text(0.5, 0.65, "TOTAL PROFIT (MARGIN 11.6%)", ha='center', va='center', fontsize=11, fontweight='bold', color=TEXT_MUTED)
    ax_kpi2.text(0.5, 0.30, "$1.47M", ha='center', va='center', fontsize=22, fontweight='bold', color=ACCENT_GREEN)
    ax_kpi2.axis('off')
    
    # KPI 3: Total Orders
    ax_kpi3 = fig.add_subplot(gs[0, 2])
    ax_kpi3.set_facecolor(CARD_BG)
    ax_kpi3.text(0.5, 0.65, "TOTAL ORDERS PLACED", ha='center', va='center', fontsize=11, fontweight='bold', color=TEXT_MUTED)
    ax_kpi3.text(0.5, 0.30, "51,271", ha='center', va='center', fontsize=22, fontweight='bold', color=ACCENT_ORANGE)
    ax_kpi3.axis('off')
    
    # KPI 4: Average Discount
    ax_kpi4 = fig.add_subplot(gs[0, 3])
    ax_kpi4.set_facecolor(CARD_BG)
    ax_kpi4.text(0.5, 0.65, "AVERAGE DISCOUNT RATE", ha='center', va='center', fontsize=11, fontweight='bold', color=TEXT_MUTED)
    ax_kpi4.text(0.5, 0.30, "14.29%", ha='center', va='center', fontsize=22, fontweight='bold', color=ACCENT_RED)
    ax_kpi4.axis('off')
    
    # Chart 1: Revenue & Profit by Market
    ax_mkt = fig.add_subplot(gs[1, 0:2])
    ax_mkt.set_facecolor(CARD_BG)
    mkt_summary = df.groupby('market').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values('sales', ascending=True)
    y_pos = np.arange(len(mkt_summary))
    ax_mkt.barh(y_pos, mkt_summary['sales']/1e6, height=0.55, color=ACCENT_BLUE, label='Revenue ($M)')
    ax_mkt.set_yticks(y_pos)
    ax_mkt.set_yticklabels(mkt_summary['market'], color=TEXT_PRIMARY, fontsize=9, fontweight='bold')
    ax_mkt.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_mkt.set_title("Market Revenue Performance (APAC & EU Leading)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_mkt.grid(axis='x', linestyle='--', alpha=0.2, color='#ffffff')
    for i, v in enumerate(mkt_summary['sales']/1e6):
        ax_mkt.text(v + 0.05, i, f"${v:.2f}M", va='center', color=TEXT_PRIMARY, fontsize=8, fontweight='bold')
    for spine in ax_mkt.spines.values(): spine.set_visible(False)
    
    # Chart 2: Category Breakdown Donut
    ax_cat = fig.add_subplot(gs[1, 2:4])
    ax_cat.set_facecolor(CARD_BG)
    cat_summary = df.groupby('category')['sales'].sum()
    wedges, texts, autotexts = ax_cat.pie(
        cat_summary, 
        labels=cat_summary.index, 
        autopct='%1.1f%%', 
        colors=[ACCENT_BLUE, ACCENT_GREEN, ACCENT_ORANGE],
        startangle=140, 
        pctdistance=0.75,
        textprops={'color': TEXT_PRIMARY, 'fontsize': 9, 'fontweight': 'bold'}
    )
    centre_circle = plt.Circle((0,0), 0.55, fc=CARD_BG)
    ax_cat.add_artist(centre_circle)
    ax_cat.set_title("Sales Share by Product Category", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    
    # Chart 3: Annual Sales & Profit Growth
    ax_yr = fig.add_subplot(gs[2, 0:3])
    ax_yr.set_facecolor(CARD_BG)
    yr_summary = df.groupby('year').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
    x = np.arange(len(yr_summary))
    ax_yr.bar(x - 0.15, yr_summary['sales']/1e6, width=0.3, color=ACCENT_BLUE, label='Sales ($M)')
    ax_yr.bar(x + 0.15, yr_summary['profit']/1e6, width=0.3, color=ACCENT_GREEN, label='Profit ($M)')
    ax_yr.set_xticks(x)
    ax_yr.set_xticklabels(yr_summary['year'], color=TEXT_PRIMARY, fontsize=9, fontweight='bold')
    ax_yr.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_yr.legend(facecolor=CARD_BG, edgecolor='none', labelcolor=TEXT_PRIMARY)
    ax_yr.set_title("Annual Growth Trajectory (YoY Expansion 2011 - 2014)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_yr.grid(axis='y', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_yr.spines.values(): spine.set_visible(False)
    
    # Chart 4: Segment Sales Gauge / Donut
    ax_seg = fig.add_subplot(gs[2, 3])
    ax_seg.set_facecolor(CARD_BG)
    seg_summary = df.groupby('segment')['sales'].sum()
    wedges2, texts2, autotexts2 = ax_seg.pie(
        seg_summary,
        labels=seg_summary.index,
        autopct='%1.0f%%',
        colors=['#7209B7', '#4361EE', '#4CC9F0'],
        startangle=90,
        pctdistance=0.75,
        textprops={'color': TEXT_PRIMARY, 'fontsize': 8, 'fontweight': 'bold'}
    )
    centre_circle2 = plt.Circle((0,0), 0.55, fc=CARD_BG)
    ax_seg.add_artist(centre_circle2)
    ax_seg.set_title("Sales by Segment", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)

    p1_path = os.path.join(out_dir, "Page-1_Executive-Overview.png")
    plt.savefig(p1_path, dpi=200, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Page 1 saved successfully.")


# -------------------------------------------------------------
# PAGE 2: SALES ANALYSIS
# -------------------------------------------------------------
def render_page2():
    fig = plt.figure(figsize=(16, 9), facecolor=BG_COLOR)
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.22)
    
    fig.text(0.04, 0.95, "PRIMEOR SOLUTIONS | GLOBAL E-COMMERCE EXECUTIVE DASHBOARD", fontsize=18, fontweight='bold', color=TEXT_PRIMARY)
    fig.text(0.04, 0.92, "Page 2: Comprehensive Sales & Geographic Analysis | Deep Dive Trends", fontsize=10, color=TEXT_MUTED)
    
    # Visual 1: Sales by Region
    ax_reg = fig.add_subplot(gs[0, 0])
    ax_reg.set_facecolor(CARD_BG)
    reg_summary = df.groupby('region')['sales'].sum().reset_index().sort_values('sales', ascending=True)
    y_reg = np.arange(len(reg_summary))
    ax_reg.barh(y_reg, reg_summary['sales']/1e6, height=0.6, color=ACCENT_BLUE)
    ax_reg.set_yticks(y_reg)
    ax_reg.set_yticklabels(reg_summary['region'], color=TEXT_PRIMARY, fontsize=8)
    ax_reg.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_reg.set_title("Sales by Global Region (Central Leads at $2.82M)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_reg.grid(axis='x', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_reg.spines.values(): spine.set_visible(False)
    
    # Visual 2: Sales by Market
    ax_mkt = fig.add_subplot(gs[0, 1])
    ax_mkt.set_facecolor(CARD_BG)
    mkt_summary = df.groupby('market').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values('sales', ascending=False)
    x_mkt = np.arange(len(mkt_summary))
    ax_mkt.bar(x_mkt, mkt_summary['sales']/1e6, width=0.5, color='#4CC9F0')
    ax_mkt.set_xticks(x_mkt)
    ax_mkt.set_xticklabels(mkt_summary['market'], color=TEXT_PRIMARY, fontsize=9, fontweight='bold')
    ax_mkt.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_mkt.set_title("Market Revenue Breakdown ($ Millions)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_mkt.grid(axis='y', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_mkt.spines.values(): spine.set_visible(False)
    
    # Visual 3: Monthly Sales Trend (48 Months)
    ax_trend = fig.add_subplot(gs[1, 0])
    ax_trend.set_facecolor(CARD_BG)
    monthly = df.groupby('year_month')['sales'].sum().reset_index()
    ax_trend.plot(np.arange(len(monthly)), monthly['sales']/1e3, color=ACCENT_GREEN, linewidth=2.2, marker='.', markersize=4)
    ax_trend.fill_between(np.arange(len(monthly)), monthly['sales']/1e3, color=ACCENT_GREEN, alpha=0.15)
    # Set tick labels every 6 months
    ticks = np.arange(0, len(monthly), 6)
    ax_trend.set_xticks(ticks)
    ax_trend.set_xticklabels(monthly['year_month'].iloc[ticks], color=TEXT_PRIMARY, fontsize=8, rotation=30)
    ax_trend.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_trend.set_title("Monthly Sales Trend (Consistent Q4 Seasonality Surge)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_trend.grid(True, linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_trend.spines.values(): spine.set_visible(False)
    
    # Visual 4: Category Performance (Sales & Profit)
    ax_cat = fig.add_subplot(gs[1, 1])
    ax_cat.set_facecolor(CARD_BG)
    cat_summary = df.groupby('category').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
    x_c = np.arange(len(cat_summary))
    ax_cat.bar(x_c - 0.15, cat_summary['sales']/1e6, width=0.3, color=ACCENT_BLUE, label='Sales ($M)')
    ax_cat.bar(x_c + 0.15, cat_summary['profit']/1e6, width=0.3, color=ACCENT_ORANGE, label='Profit ($M)')
    ax_cat.set_xticks(x_c)
    ax_cat.set_xticklabels(cat_summary['category'], color=TEXT_PRIMARY, fontsize=9, fontweight='bold')
    ax_cat.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_cat.legend(facecolor=CARD_BG, edgecolor='none', labelcolor=TEXT_PRIMARY)
    ax_cat.set_title("Category Performance (Technology Highest Net Margin)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_cat.grid(axis='y', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_cat.spines.values(): spine.set_visible(False)

    p2_path = os.path.join(out_dir, "Page-2_Sales-Analysis.png")
    plt.savefig(p2_path, dpi=200, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Page 2 saved successfully.")


# -------------------------------------------------------------
# PAGE 3: PRODUCT & CUSTOMER INSIGHTS
# -------------------------------------------------------------
def render_page3():
    fig = plt.figure(figsize=(16, 9), facecolor=BG_COLOR)
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.25)
    
    fig.text(0.04, 0.95, "PRIMEOR SOLUTIONS | GLOBAL E-COMMERCE EXECUTIVE DASHBOARD", fontsize=18, fontweight='bold', color=TEXT_PRIMARY)
    fig.text(0.04, 0.92, "Page 3: Assortment Profitability & Key Customer Accounts", fontsize=10, color=TEXT_MUTED)
    
    # Visual 1: Top 10 Products by Sales
    ax_prod = fig.add_subplot(gs[0, 0])
    ax_prod.set_facecolor(CARD_BG)
    top_p = df.groupby('product_name')['sales'].sum().reset_index().sort_values('sales', ascending=True).tail(10)
    y_p = np.arange(len(top_p))
    short_names = [n[:28] + '...' if len(n) > 28 else n for n in top_p['product_name']]
    ax_prod.barh(y_p, top_p['sales']/1e3, height=0.6, color='#7209B7')
    ax_prod.set_yticks(y_p)
    ax_prod.set_yticklabels(short_names, color=TEXT_PRIMARY, fontsize=8)
    ax_prod.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_prod.set_title("Top 10 Products by Revenue ($k)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_prod.grid(axis='x', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_prod.spines.values(): spine.set_visible(False)
    
    # Visual 2: Top 10 Customers by Sales
    ax_cust = fig.add_subplot(gs[0, 1])
    ax_cust.set_facecolor(CARD_BG)
    top_c = df.groupby('customer_name')['sales'].sum().reset_index().sort_values('sales', ascending=True).tail(10)
    y_c = np.arange(len(top_c))
    ax_cust.barh(y_c, top_c['sales']/1e3, height=0.6, color=ACCENT_BLUE)
    ax_cust.set_yticks(y_c)
    ax_cust.set_yticklabels(top_c['customer_name'], color=TEXT_PRIMARY, fontsize=8)
    ax_cust.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_cust.set_title("Top 10 High-Spending Customers ($k)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_cust.grid(axis='x', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_cust.spines.values(): spine.set_visible(False)
    
    # Visual 3: Profit by Sub-Category (Highlighting Tables Loss)
    ax_sub = fig.add_subplot(gs[1, 0])
    ax_sub.set_facecolor(CARD_BG)
    sub_summary = df.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=True)
    y_s = np.arange(len(sub_summary))
    bar_colors = [ACCENT_RED if val < 0 else ACCENT_GREEN for val in sub_summary['profit']]
    ax_sub.barh(y_s, sub_summary['profit']/1e3, height=0.65, color=bar_colors)
    ax_sub.set_yticks(y_s)
    ax_sub.set_yticklabels(sub_summary['sub_category'], color=TEXT_PRIMARY, fontsize=8)
    ax_sub.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_sub.set_title("Profit by Sub-Category (Tables Severe Loss: -$64k)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_sub.axvline(0, color=TEXT_MUTED, linestyle='--', linewidth=0.8)
    ax_sub.grid(axis='x', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_sub.spines.values(): spine.set_visible(False)
    
    # Visual 4: Segment Analysis (Sales & Profit Comparison)
    ax_seg = fig.add_subplot(gs[1, 1])
    ax_seg.set_facecolor(CARD_BG)
    seg_summary = df.groupby('segment').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
    x_s = np.arange(len(seg_summary))
    ax_seg.bar(x_s - 0.15, seg_summary['sales']/1e6, width=0.3, color=ACCENT_BLUE, label='Sales ($M)')
    ax_seg.bar(x_s + 0.15, seg_summary['profit']/1e6, width=0.3, color=ACCENT_GREEN, label='Profit ($M)')
    ax_seg.set_xticks(x_s)
    ax_seg.set_xticklabels(seg_summary['segment'], color=TEXT_PRIMARY, fontsize=9, fontweight='bold')
    ax_seg.tick_params(colors=TEXT_MUTED, labelsize=8)
    ax_seg.legend(facecolor=CARD_BG, edgecolor='none', labelcolor=TEXT_PRIMARY)
    ax_seg.set_title("Segment Performance (Consumer Drives 51.5% Sales)", fontsize=11, fontweight='bold', color=TEXT_PRIMARY, pad=10)
    ax_seg.grid(axis='y', linestyle='--', alpha=0.2, color='#ffffff')
    for spine in ax_seg.spines.values(): spine.set_visible(False)

    p3_path = os.path.join(out_dir, "Page-3_Product-and-Customer-Insights.png")
    plt.savefig(p3_path, dpi=200, bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Page 3 saved successfully.")

if __name__ == '__main__':
    render_page1()
    render_page2()
    render_page3()
    print("All 3 dashboard mockup pages rendered successfully.")
