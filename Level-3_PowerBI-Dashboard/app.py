import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Primeor Solutions - Power BI Interactive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Executive Theme CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0B132B;
        color: #FFFFFF;
    }
    .metric-card {
        background-color: #1C2541;
        border: 1px solid #2A385B;
        border-radius: 10px;
        padding: 16px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        text-align: center;
    }
    .metric-title {
        color: #8D99AE;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 700;
    }
    .stSelectbox label, .stMultiSelect label {
        color: #8D99AE !important;
        font-weight: 600;
    }
    div[data-testid="stSidebar"] {
        background-color: #0E1626;
        border-right: 1px solid #1C2541;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../dataset/cleaned/cleaned_ecommerce_dataset.csv"))
    df = pd.read_csv(csv_path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['ship_date'] = pd.to_datetime(df['ship_date'])
    df['year_month'] = df['order_date'].dt.to_period('M').astype(str)
    return df

df_raw = load_data()

# -------------------------------------------------------------
# SIDEBAR: SLICERS & FILTERS
# -------------------------------------------------------------
st.sidebar.image("https://img.shields.io/badge/Primeor%20Solutions-Data%20Analytics%20Internship-3A86FF?style=for-the-badge", use_container_width=True)
st.sidebar.title("🎛️ Dashboard Slicers")

# Navigation Selector
page = st.sidebar.radio(
    "📑 Select Dashboard Page:",
    ["Page 1: Executive Overview", "Page 2: Sales Analysis", "Page 3: Product & Customer Insights"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Interactive Filters")

# Year Slicer
available_years = sorted(df_raw['year'].unique())
selected_years = st.sidebar.multiselect("Calendar Year:", available_years, default=available_years)

# Market Slicer
available_markets = sorted(df_raw['market'].unique())
selected_markets = st.sidebar.multiselect("Global Market:", available_markets, default=available_markets)

# Category Slicer
available_categories = sorted(df_raw['category'].unique())
selected_categories = st.sidebar.multiselect("Product Category:", available_categories, default=available_categories)

# Segment Slicer
available_segments = sorted(df_raw['segment'].unique())
selected_segments = st.sidebar.multiselect("Customer Segment:", available_segments, default=available_segments)

# Apply Filter Mask
filtered_df = df_raw[
    (df_raw['year'].isin(selected_years)) &
    (df_raw['market'].isin(selected_markets)) &
    (df_raw['category'].isin(selected_categories)) &
    (df_raw['segment'].isin(selected_segments))
]

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected filters. Please expand your selections.")
    st.stop()

# Plotly Theme Defaults
THEME_PLOTLY = {
    "layout": {
        "paper_bgcolor": "#1C2541",
        "plot_bgcolor": "#1C2541",
        "font": {"color": "#FFFFFF", "family": "Segoe UI, sans-serif"},
        "margin": {"l": 40, "r": 30, "t": 45, "b": 40},
        "xaxis": {"gridcolor": "rgba(255,255,255,0.08)", "zerolinecolor": "rgba(255,255,255,0.15)"},
        "yaxis": {"gridcolor": "rgba(255,255,255,0.08)", "zerolinecolor": "rgba(255,255,255,0.15)"}
    }
}

# -------------------------------------------------------------
# PAGE 1: EXECUTIVE OVERVIEW
# -------------------------------------------------------------
if page == "Page 1: Executive Overview":
    st.title("📊 Page 1 — Executive Overview")
    st.caption("Primeor Solutions E-Commerce Analytics | C-Suite KPI Performance Summary")
    
    # 4 Core KPI Cards
    total_sales = filtered_df['sales'].sum()
    total_profit = filtered_df['profit'].sum()
    total_orders = filtered_df['order_id'].nunique()
    avg_discount = filtered_df['discount'].mean() * 100
    profit_margin = (total_profit / total_sales * 100) if total_sales else 0
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Sales Revenue</div>
            <div class="metric-value" style="color: #3A86FF;">${total_sales:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Net Profit ({profit_margin:.1f}% Margin)</div>
            <div class="metric-value" style="color: #06D6A0;">${total_profit:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Total Orders Placed</div>
            <div class="metric-value" style="color: #FFB703;">{total_orders:,}</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Average Applied Discount</div>
            <div class="metric-value" style="color: #EF476F;">{avg_discount:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 1 Visuals
    r1_col1, r1_col2 = st.columns([1.5, 1])
    
    with r1_col1:
        mkt_df = filtered_df.groupby('market').agg({'sales': 'sum', 'profit': 'sum'}).reset_index().sort_values('sales', ascending=True)
        fig_mkt = px.bar(
            mkt_df,
            x='sales',
            y='market',
            orientation='h',
            title="<b>Market Revenue Performance ($)</b>",
            color='sales',
            color_continuous_scale=['#1C2541', '#3A86FF'],
            text_auto='.2s'
        )
        fig_mkt.update_layout(**THEME_PLOTLY['layout'], coloraxis_showscale=False)
        st.plotly_chart(fig_mkt, use_container_width=True)
        
    with r1_col2:
        cat_df = filtered_df.groupby('category')['sales'].sum().reset_index()
        fig_cat = px.pie(
            cat_df,
            names='category',
            values='sales',
            title="<b>Sales Contribution by Category</b>",
            hole=0.55,
            color_discrete_sequence=['#3A86FF', '#06D6A0', '#FFB703']
        )
        fig_cat.update_layout(**THEME_PLOTLY['layout'])
        st.plotly_chart(fig_cat, use_container_width=True)
        
    # Row 2 Visuals
    r2_col1, r2_col2 = st.columns([1.5, 1])
    
    with r2_col1:
        yr_df = filtered_df.groupby('year').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
        fig_yr = go.Figure()
        fig_yr.add_trace(go.Bar(x=yr_df['year'], y=yr_df['sales'], name='Revenue ($)', marker_color='#3A86FF'))
        fig_yr.add_trace(go.Bar(x=yr_df['year'], y=yr_df['profit'], name='Profit ($)', marker_color='#06D6A0'))
        fig_yr.update_layout(
            barmode='group',
            title="<b>Annual Performance Trajectory (YoY Growth)</b>",
            **THEME_PLOTLY['layout'],
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_yr, use_container_width=True)
        
    with r2_col2:
        seg_df = filtered_df.groupby('segment')['sales'].sum().reset_index()
        fig_seg = px.pie(
            seg_df,
            names='segment',
            values='sales',
            title="<b>Sales by Customer Segment</b>",
            hole=0.55,
            color_discrete_sequence=['#7209B7', '#4361EE', '#4CC9F0']
        )
        fig_seg.update_layout(**THEME_PLOTLY['layout'])
        st.plotly_chart(fig_seg, use_container_width=True)


# -------------------------------------------------------------
# PAGE 2: SALES ANALYSIS
# -------------------------------------------------------------
elif page == "Page 2: Sales Analysis":
    st.title("📈 Page 2 — Sales Analysis")
    st.caption("Primeor Solutions E-Commerce Analytics | Geographic Breakdown & Time-Series Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        reg_df = filtered_df.groupby('region')['sales'].sum().reset_index().sort_values('sales', ascending=True)
        fig_reg = px.bar(
            reg_df,
            x='sales',
            y='region',
            orientation='h',
            title="<b>Sales by Global Region ($)</b>",
            color_discrete_sequence=['#3A86FF'],
            text_auto='.2s'
        )
        fig_reg.update_layout(**THEME_PLOTLY['layout'])
        st.plotly_chart(fig_reg, use_container_width=True)
        
    with col2:
        mkt_bar = filtered_df.groupby('market')['sales'].sum().reset_index().sort_values('sales', ascending=False)
        fig_mkt_bar = px.bar(
            mkt_bar,
            x='market',
            y='sales',
            title="<b>Sales by Market ($)</b>",
            color_discrete_sequence=['#4CC9F0'],
            text_auto='.2s'
        )
        fig_mkt_bar.update_layout(**THEME_PLOTLY['layout'])
        st.plotly_chart(fig_mkt_bar, use_container_width=True)
        
    col3, col4 = st.columns(2)
    
    with col3:
        trend_df = filtered_df.groupby('year_month')['sales'].sum().reset_index()
        fig_trend = px.area(
            trend_df,
            x='year_month',
            y='sales',
            title="<b>Monthly Sales Trend (Consistent Q4 Seasonality Surge)</b>",
            color_discrete_sequence=['#06D6A0']
        )
        fig_trend.update_layout(**THEME_PLOTLY['layout'], xaxis_title="Order Year-Month", yaxis_title="Sales ($)")
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with col4:
        cat_perf = filtered_df.groupby('category').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
        fig_cat_perf = go.Figure()
        fig_cat_perf.add_trace(go.Bar(x=cat_perf['category'], y=cat_perf['sales'], name='Sales ($)', marker_color='#3A86FF'))
        fig_cat_perf.add_trace(go.Bar(x=cat_perf['category'], y=cat_perf['profit'], name='Profit ($)', marker_color='#FFB703'))
        fig_cat_perf.update_layout(
            barmode='group',
            title="<b>Category Performance: Sales vs. Net Profit</b>",
            **THEME_PLOTLY['layout'],
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_cat_perf, use_container_width=True)


# -------------------------------------------------------------
# PAGE 3: PRODUCT & CUSTOMER INSIGHTS
# -------------------------------------------------------------
elif page == "Page 3: Product & Customer Insights":
    st.title("🔍 Page 3 — Product & Customer Insights")
    st.caption("Primeor Solutions E-Commerce Analytics | Assortment Profitability & Account Management")
    
    c1, c2 = st.columns(2)
    
    with c1:
        top_p = filtered_df.groupby('product_name')['sales'].sum().reset_index().sort_values('sales', ascending=True).tail(10)
        top_p['short_name'] = top_p['product_name'].apply(lambda x: x[:30] + '...' if len(x) > 30 else x)
        fig_p = px.bar(
            top_p,
            x='sales',
            y='short_name',
            orientation='h',
            title="<b>Top 10 Products by Sales Revenue ($)</b>",
            color_discrete_sequence=['#7209B7'],
            text_auto='.2s'
        )
        fig_p.update_layout(**THEME_PLOTLY['layout'], yaxis_title="")
        st.plotly_chart(fig_p, use_container_width=True)
        
    with c2:
        top_c = filtered_df.groupby('customer_name')['sales'].sum().reset_index().sort_values('sales', ascending=True).tail(10)
        fig_c = px.bar(
            top_c,
            x='sales',
            y='customer_name',
            orientation='h',
            title="<b>Top 10 Customers by Lifetime Sales ($)</b>",
            color_discrete_sequence=['#3A86FF'],
            text_auto='.2s'
        )
        fig_c.update_layout(**THEME_PLOTLY['layout'], yaxis_title="")
        st.plotly_chart(fig_c, use_container_width=True)
        
    c3, c4 = st.columns(2)
    
    with c3:
        sub_df = filtered_df.groupby('sub_category')['profit'].sum().reset_index().sort_values('profit', ascending=True)
        sub_df['color'] = sub_df['profit'].apply(lambda x: '#EF476F' if x < 0 else '#06D6A0')
        fig_sub = go.Figure(go.Bar(
            x=sub_df['profit'],
            y=sub_df['sub_category'],
            orientation='h',
            marker_color=sub_df['color'],
            text=[f"${v:,.0f}" for v in sub_df['profit']],
            textposition='outside'
        ))
        fig_sub.update_layout(
            title="<b>Profit by Sub-Category (Severe Tables Losses: -$64k)</b>",
            **THEME_PLOTLY['layout'],
            yaxis_title=""
        )
        st.plotly_chart(fig_sub, use_container_width=True)
        
    with c4:
        seg_p = filtered_df.groupby('segment').agg({'sales': 'sum', 'profit': 'sum'}).reset_index()
        fig_seg_p = go.Figure()
        fig_seg_p.add_trace(go.Bar(x=seg_p['segment'], y=seg_p['sales'], name='Sales ($)', marker_color='#3A86FF'))
        fig_seg_p.add_trace(go.Bar(x=seg_p['segment'], y=seg_p['profit'], name='Profit ($)', marker_color='#06D6A0'))
        fig_seg_p.update_layout(
            barmode='group',
            title="<b>Segment Performance: Sales vs. Profit</b>",
            **THEME_PLOTLY['layout'],
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_seg_p, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #8D99AE; font-size: 0.85rem;'>Primeor Solutions Data Analytics Internship | Developed by Rishi Prajapati</p>", unsafe_allow_html=True)
