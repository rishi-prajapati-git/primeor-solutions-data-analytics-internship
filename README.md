# Primeor Solutions - E-Commerce Data Analytics Internship

[![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
[![Excel](https://img.shields.io/badge/Tools-Excel%20%7C%20Python%20%7C%20SQL%20%7C%20PowerBI-success.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
[![Status](https://img.shields.io/badge/Status-All%20Levels%20Completed%20(100%25)-brightgreen.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)

Comprehensive business analytics and reporting project completed as part of the **Primeor Solutions Data Analytics Internship Program**. This repository houses all project milestones across **Level 1 (Excel Data Cleaning & Analysis)**, **Level 2 (SQL Analytics & Insights)**, and **Level 3 (Interactive Power BI Dashboards)**.

---

## 📌 Project Overview & Roadmap

| Level | Topic | Status | Key Deliverables |
| :--- | :--- | :---: | :--- |
| **Level 1** | **Data Understanding & Cleaning (Excel)** | ✅ **Completed** | Cleaned dataset (51,271 records), Excel KPI models, Pivot tables, charts & reports |
| **Level 2** | **Data Analysis (SQL)** | ✅ **Completed** | SQL database schema, portable SQLite DB, 10 business analytical queries, results workbook & insights report |
| **Level 3** | **Power BI Dashboard & Visualizations** | ✅ **Completed** | 3-page interactive `.pbix` / `.pbit` dashboard, DAX metrics, visual layouts & executive PDF report |

---

## 📂 Repository Directory Structure

```text
primeor-solutions-data-analytics-internship/
│
├── dataset/
│   ├── raw/
│   │   └── Dataset.csv                             # Original raw dataset (51,325 rows)
│   └── cleaned/
│       └── cleaned_ecommerce_dataset.csv           # Deduplicated, normalized dataset (51,271 rows)
│
├── Level-1_Data-Cleaning-and-Excel-Analysis/
│   ├── Task-1_Data-Cleaning/
│   │   ├── clean_data.py                           # Automated Python data cleaning script
│   │   └── data_cleaning_report.md                 # Detailed data cleaning & audit report
│   ├── Task-2_Basic-Excel-Analysis/
│   │   └── basic_analysis_metrics.md               # KPI cards, top/bottom product analysis & formula docs
│   ├── Task-3_Pivot-Tables-and-Charts/
│   │   ├── charts/                                 # High-resolution charts (PNG)
│   │   │   ├── sales_by_region.png
│   │   │   ├── profit_by_category.png
│   │   │   ├── segment_wise_sales.png
│   │   │   └── monthly_sales_trend.png
│   │   └── pivot_tables_and_charts_report.md       # Visual analytical report
│   ├── Ecommerce_Analysis_Level1.xlsx              # Complete Excel workbook with formulas & embedded charts
│   └── generate_level1_workbook.py                 # Script generating the comprehensive Excel workbook
│
├── Level-2_SQL-Data-Analysis/
│   ├── Task-1_Import-Data-into-SQL/
│   │   ├── schema_and_setup.sql                    # Production DDL schema for MySQL, PostgreSQL & SQLite
│   │   ├── import_to_sqlite.py                     # Python ETL pipeline populating local database
│   │   └── data_import_documentation.md            # Database schema & ingestion guide
│   ├── Task-2_SQL-Queries/
│   │   ├── all_level2_queries.sql                  # 10 production SQL business queries
│   │   ├── export_query_results.py                 # Automated query execution & Excel exporter
│   │   ├── sql_query_results.xlsx                  # 10-sheet structured Excel workbook with query outputs
│   │   └── sql_queries_and_results_documentation.md# Complete query explanations & result tables
│   ├── Task-3_SQL-Insights-Report/
│   │   ├── charts/                                 # Analytical charts (PNG)
│   │   │   ├── market_revenue_profit.png
│   │   │   ├── ship_mode_distribution.png
│   │   │   └── category_profit_margin.png
│   │   ├── generate_pdf_report.py                  # Automated ReportLab PDF generator script
│   │   ├── Level2_SQL_Business_Insights_Report.pdf # Executive PDF Business Insights Report (Submission Requirement)
│   │   └── sql_business_insights_report.md         # Comprehensive executive business insights & strategy
│   └── ecommerce_analysis.db                       # Pre-built SQLite database for zero-config evaluation
│
├── Level-3_PowerBI-Dashboard/
│   ├── Task-1_Interactive-Dashboard-Pages/
│   │   ├── dax_data_model_and_measures.dax         # Complete Power Query M-code & organized DAX measures
│   │   └── dashboard_pages_specification.md        # Technical data bindings for Pages 1, 2, and 3
│   ├── Task-2_Dashboard-Features-and-Theme/
│   │   ├── Primeor_Executive_Theme.json            # Custom executive midnight theme palette
│   │   ├── dashboard_features_and_theme_specification.md # Interactive slicers & UX architecture
│   │   ├── generate_level3_pdf.py                  # Automated ReportLab Level 3 PDF generator script
│   │   └── Level3_PowerBI_Dashboard_Report.pdf     # 3-Page Executive Power BI Presentation & PDF Report
│   ├── dashboard_mockups/                          # Ultra HD rendered layout visuals
│   │   ├── Page-1_Executive-Overview.png
│   │   ├── Page-2_Sales-Analysis.png
│   │   ├── Page-3_Product-and-Customer-Insights.png
│   │   └── generate_dashboard_mockups.py
│   ├── pbit_template/
│   │   └── build_pbi_package.py                    # Open packaging script generating .pbit and .pbix
│   ├── Ecommerce_Analysis_Level3.pbit              # Power BI Template with pre-configured visuals & theme
│   └── Ecommerce_Analysis_Level3.pbix              # Standalone Power BI Report Package
│
├── README.md
└── .gitignore
```

---

## 📊 Level 1: Excel Analytics Summary

### Executive KPIs
- **Total Sales:** **$12,635,222.00**
- **Total Profit:** **$1,467,721.69** (Profit Margin: **11.62%**)
- **Average Discount:** **14.29%**
- **Total Clean Records:** **51,271** (54 duplicates removed, 0 null values remaining)

---

## 🗄️ Level 2: SQL Analytics Summary & Insights

### Core Business Findings:
1. **Highest Revenue Market:**  
   **APAC (Asia-Pacific)** leads globally with **$3,581,785.00** in total revenue (28.35% revenue share) and **$437,023.52** in profit, followed by the **EU** ($2.94M, 23.25%).
2. **Least Profitable Category:**  
   **Furniture** is the lowest margin category at **6.97%** ($29.00 avg profit/order). At the sub-category level, **Tables** produced a devastating loss of **-$64,113.55** (-8.48% margin) due to deep discounting (avg > 35%) and high freight overhead.
3. **Most Commonly Used Shipping Mode:**  
   **Standard Class** accounts for **60.00%** of all shipments (30,764 orders), followed by Second Class (20.10%), First Class (14.64%), and Same Day (5.26%).
4. **Loss-Making Orders Impact:**  
   **12,534 orders (24.45%)** were executed at a loss, accumulating **-$518,633.91** in negative earnings. The average discount on loss-making orders was **45.08%**, proving that unrestrained discounting is the single primary margin destroyer.

---

## 📱 Level 3: Power BI Dashboard & Visualizations

The Power BI Dashboard consists of 3 purpose-built reporting pages styled with the **Primeor Executive Theme**:

### Page 1 — Executive Overview
- **Core KPI Cards:** Total Sales ($12.64M), Total Profit ($1.47M), Total Orders (51,271), and Average Discount (14.29%).
- **Market Revenue:** Horizontal bar chart comparing global market contributions.
- **Category Sales:** Donut chart illustrating sales distribution across Technology, Furniture, and Office Supplies.
- **YoY Growth:** Annual clustered bar charts showing progression from 2011 to 2014.

### Page 2 — Sales Analysis
- **Geographic Breakdown:** Sales by Region (13 regions) and Market.
- **Monthly Sales Trend:** 48-month continuous area chart demonstrating annual Q4 peaks.
- **Category Comparison:** Side-by-side clustered column chart comparing Sales vs Profit.

### Page 3 — Product & Customer Insights
- **Top 10 Products:** Highest-grossing items led by Apple and Cisco smartphones.
- **Top 10 Customers:** High-spending accounts led by Tom Ashbrook ($40.5k).
- **Profit by Sub-Category:** Diverging bar chart identifying high performers (Copiers, Phones) and severe losses (Tables: -$64k).
- **Customer Segments:** Sales and margin breakdown across Consumer (51.5%), Corporate (30.3%), and Home Office (18.2%).

---

## 👤 Author
- **Rishi Prajapati**  
- **Role:** Data Analytics Intern  
- **Organization:** Primeor Solutions  
