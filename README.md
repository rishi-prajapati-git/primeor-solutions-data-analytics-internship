# Primeor Solutions — Global E-Commerce Data Analytics Internship

[![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
[![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20Python%20%7C%20SQLite%20%7C%20PowerBI%20%7C%20Streamlit-success.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
[![Status](https://img.shields.io/badge/Status-100%25%20Completed%20%26%20Verified-brightgreen.svg)](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
[![Author](https://img.shields.io/badge/Author-Rishi%20Prajapati-orange.svg)](https://github.com/rishi-prajapati-git)

Comprehensive end-to-end data analytics and business intelligence project completed for the **Primeor Solutions Data Analytics Internship Program**. This repository houses all project milestones across **Level 1 (Excel Data Cleaning & Analysis)**, **Level 2 (SQL Analytics & Insights)**, and **Level 3 (Interactive Power BI Dashboard & Visual Intelligence)**.

---

## 📌 Executive Summary

Across **51,271 verified transactional records** spanning 2011 to 2014, global operations achieved **$12,635,222.00** in gross revenue and **$1,467,721.69** in net operating profit (11.62% net profit margin). 

Empirical analysis across 7 international markets, 13 geographic regions, and 4 fulfillment modes identified high-margin growth hubs (APAC & EU driving **51.6%** of revenue) while exposing deep discounting practices that drained **-$518,633.91** in accumulated losses across 12,534 transactions.

---

## 🗺️ Project Roadmap & Completion Status

| Milestone | Domain & Focus | Status | Primary Deliverables |
| :--- | :--- | :---: | :--- |
| **Level 1** | **Data Understanding & Cleaning (Excel)** | ✅ **100% Completed** | Deduplicated dataset (51,271 rows), Excel KPI formulas, Pivot tables, visual charts & comprehensive workbook |
| **Level 2** | **Data Analysis & Relational Engine (SQL)** | ✅ **100% Completed** | Database DDL schema, SQLite database, 10 core business SQL queries, multi-sheet Excel export & executive PDF report |
| **Level 3** | **Interactive Dashboard & Business Intelligence (Power BI)** | ✅ **100% Completed** | 3-page interactive `.pbix` / `.pbit` dashboard, DAX measures, modern web app UI & 3-page presentation PDF report |

---

## 📂 Repository Architecture

```text
primeor-solutions-data-analytics-internship/
│
├── dataset/
│   ├── raw/
│   │   └── Dataset.csv                             # Original raw dataset (51,325 rows)
│   └── cleaned/
│       └── cleaned_ecommerce_dataset.csv           # Normalized dataset (51,271 rows, 0 nulls, 0 duplicates)
│
├── Level-1_Data-Cleaning-and-Excel-Analysis/
│   ├── Task-1_Data-Cleaning/
│   │   ├── clean_data.py                           # Python data cleaning & deduplication pipeline
│   │   └── data_cleaning_report.md                 # Data quality audit & validation documentation
│   ├── Task-2_Basic-Excel-Analysis/
│   │   └── basic_analysis_metrics.md               # KPI formulas, top 5 & loss-making product tables
│   ├── Task-3_Pivot-Tables-and-Charts/
│   │   ├── charts/                                 # High-resolution analytical charts (PNG)
│   │   │   ├── sales_by_region.png
│   │   │   ├── profit_by_category.png
│   │   │   ├── segment_wise_sales.png
│   │   │   └── monthly_sales_trend.png
│   │   └── pivot_tables_and_charts_report.md       # Visual analytical report
│   ├── Ecommerce_Analysis_Level1.xlsx              # Complete Excel workbook with formulas & embedded charts
│   └── generate_level1_workbook.py                 # Automated openpyxl workbook generator script
│
├── Level-2_SQL-Data-Analysis/
│   ├── Task-1_Import-Data-into-SQL/
│   │   ├── schema_and_setup.sql                    # Production DDL schema for MySQL, PostgreSQL & SQLite
│   │   ├── import_to_sqlite.py                     # Automated SQLite ingestion pipeline
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
│   │   ├── dax_data_model_and_measures.dax         # Power Query M-code & organized DAX measures
│   │   └── dashboard_pages_specification.md        # Technical data bindings for Pages 1, 2, and 3
│   ├── Task-2_Dashboard-Features-and-Theme/
│   │   ├── Primeor_Executive_Theme.json            # Executive color theme palette
│   │   ├── dashboard_features_and_theme_specification.md # Interactive slicers & UX architecture
│   │   ├── generate_level3_pdf.py                  # Automated ReportLab Level 3 PDF generator script
│   │   └── Level3_PowerBI_Dashboard_Report.pdf     # 3-Page Executive Power BI Presentation & PDF Report
│   ├── dashboard_mockups/                          # Ultra HD visual layouts
│   │   ├── Page-1_Executive-Overview.png
│   │   ├── Page-2_Sales-Analysis.png
│   │   ├── Page-3_Product-and-Customer-Insights.png
│   │   └── generate_dashboard_mockups.py
│   ├── pbit_template/
│   │   └── build_pbi_package.py                    # Script generating .pbit and .pbix packages
│   ├── app.py                                      # Modern interactive web dashboard application
│   ├── Ecommerce_Analysis_Level3.pbit              # Power BI Template with pre-configured visuals & theme
│   └── Ecommerce_Analysis_Level3.pbix              # Standalone Power BI Report Package
│
├── README.md
└── .gitignore
```

---

## 📊 Level 1: Excel Data Cleaning & Basic Analysis

### Key Milestones Achieved:
1. **Deduplication & Data Normalization:** Identified and purged 54 duplicate rows from raw 51,325 records. Zero missing/null values remaining across 51,271 clean rows.
2. **Executive KPI Modeling:**
   - **Total Sales:** `$12,635,222.00` (Calculated via Excel `=SUM(sales)`)
   - **Total Profit:** `$1,467,721.69` (Net profit margin: `11.62%`)
   - **Average Applied Discount:** `14.29%`
3. **Product Extremes:**
   - *Top Sales Product:* Apple Smart Phone Full Size (`$86,935.78` sales)
   - *Top Loss Product:* Cubify CubeX 3D Printer Double Head (`-$8,879.97` net loss)
4. **Pivot Tables & Visual Reporting:** Multi-sheet formatted Excel workbook (`Ecommerce_Analysis_Level1.xlsx`) with embedded charts for regional distribution, monthly trends, and segment breakdowns.

---

## 🗄️ Level 2: SQL Data Analysis & Business Insights

### Core Analytical Inquiries Addressed:
1. **Highest Revenue Market:**  
   **APAC (Asia-Pacific)** leads globally with **$3,581,785.00** in gross revenue (28.35% revenue share) and **$437,023.52** in net profit, followed closely by the **EU** ($2.94M, 23.25%).
2. **Least Profitable Category:**  
   **Furniture** is the lowest margin category at **6.97%** ($29.00 profit/order). At the sub-category level, **Tables** produced devastating net losses of **-$64,113.55** (-8.48% margin) due to deep discounting (avg > 35%) and heavy shipping overhead.
3. **Most Commonly Used Shipping Mode:**  
   **Standard Class** accounts for **60.00%** of all shipments (30,764 orders), followed by Second Class (20.10%), First Class (14.64%), and Same Day (5.26%).
4. **Bleeding Transaction Root-Cause Audit:**  
   **12,534 orders (24.45%)** were closed at a loss, accumulating **-$518,633.91** in negative earnings. The average discount on loss-making orders was **45.08%** (versus only 4.38% on profitable orders), confirming promotional over-discounting as the primary profit drain.

---

## 📱 Level 3: Power BI Interactive Dashboard

The dashboard consists of 3 purpose-built reporting pages with synchronized multi-dimensional slicers (Year, Market, Category, Segment):

### Page 1 — Executive Overview
- **Executive KPI Cards:** Total Sales ($12.64M), Total Profit ($1.47M), Total Orders (51,271), Average Discount (14.29%).
- **Market Revenue:** Horizontal bar chart comparing global market contributions.
- **Category Sales:** Donut chart illustrating sales distribution across Technology, Furniture, and Office Supplies.
- **YoY Growth:** Annual clustered bar charts showing progression from 2011 to 2014.

### Page 2 — Sales Analysis
- **Geographic Breakdown:** Sales by Region (13 regions) and Market.
- **Monthly Sales Trend:** 48-month continuous area chart demonstrating recurring Q4 surges.
- **Category Comparison:** Side-by-side clustered column chart comparing Sales vs Profit.

### Page 3 — Product & Customer Insights
- **Top 10 Products:** Highest-grossing items led by Apple and Cisco smartphones.
- **Top 10 Customers:** High-spending accounts led by Tom Ashbrook ($40.5k).
- **Profit by Sub-Category:** Diverging bar chart identifying high performers (Copiers, Phones) and severe losses (Tables: -$64k).
- **Customer Segments:** Sales and margin breakdown across Consumer (51.5%), Corporate (30.3%), and Home Office (18.2%).

---

## 🚀 How to Run the Project & Interactive Dashboard

Samne wale evaluator / mentor ke paas dashboard check karne ke **3 aasan tareeqe** hain:

### Method 1: One-Click Desktop Launcher (Sabse Simple ⚡)
Agar repository download/clone ki hui hai, toh bas root folder me:
- **`run_dashboard.bat`** par double click karo!
- Dependencies apne aap verify hongi aur browser me live interactive dashboard khul jayega (`http://localhost:8501`).

---

### Method 2: Terminal / Command Prompt se Run karna
Kisi bhi terminal (CMD ya PowerShell) me ye 2 commands chalao:

```bash
# 1. Install required packages
pip install pandas plotly streamlit openpyxl reportlab

# 2. Run the interactive dashboard
python -m streamlit run "Level-3_PowerBI-Dashboard/app.py"
```
Browser turant `http://localhost:8501` par live dynamic filters aur interactive charts open kar dega.

---

### Method 3: Official Power BI Desktop se Open karna (.pbix)
Agar evaluator Power BI Desktop user hai:
1. File locate kare: [`Level-3_PowerBI-Dashboard/Ecommerce_Analysis_Level3.pbix`](file:///c:/Users/praja/Downloads/Primeor%20Solutions%20Intern/Level-3_PowerBI-Dashboard/Ecommerce_Analysis_Level3.pbix)
2. Double click karke **Power BI Desktop** me open kare.
3. Teeno pages (`Page 1 - Executive Overview`, `Page 2 - Sales Analysis`, `Page 3 - Product & Customer Insights`) visual model ke sath ready hain.

---

### Method 4: Zero-Setup Presentation PDF
Agar kisi ke system me software nahi hai:
- Direct open kare: [`Level-3_PowerBI-Dashboard/Task-2_Dashboard-Features-and-Theme/Level3_PowerBI_Dashboard_Report.pdf`](file:///c:/Users/praja/Downloads/Primeor%20Solutions%20Intern/Level-3_PowerBI-Dashboard/Task-2_Dashboard-Features-and-Theme/Level3_PowerBI_Dashboard_Report.pdf) jisme sare 3 pages ke high-definition mockups, KPI tables aur analysis pehle se documented hain.

Open your browser at `http://localhost:8501` to explore the live dashboard with interactive filters, staged 3D visual frames, and dynamic KPI calculations.

---

## 📋 Final Submission Package Checklist

As required by the Primeor Solutions project guidelines:
- [x] **Cleaned Dataset:** `dataset/cleaned/cleaned_ecommerce_dataset.csv`
- [x] **SQL Queries File:** `Level-2_SQL-Data-Analysis/Task-2_SQL-Queries/all_level2_queries.sql`
- [x] **Excel Analysis File:** `Level-1_Data-Cleaning-and-Excel-Analysis/Ecommerce_Analysis_Level1.xlsx`
- [x] **Power BI Dashboard:** `Level-3_PowerBI-Dashboard/Ecommerce_Analysis_Level3.pbix` (and `.pbit`)
- [x] **Final Business Insights Reports (PDF):**
  - SQL Insights: `Level-2_SQL-Data-Analysis/Task-3_SQL-Insights-Report/Level2_SQL_Business_Insights_Report.pdf`
  - Power BI Presentation: `Level-3_PowerBI-Dashboard/Task-2_Dashboard-Features-and-Theme/Level3_PowerBI_Dashboard_Report.pdf`

---

## 👤 Author & Contact
- **Rishi Prajapati**  
- **Role:** Data Analytics Intern  
- **Organization:** Primeor Solutions  
- **GitHub:** [@rishi-prajapati-git](https://github.com/rishi-prajapati-git)  
- **Repository:** [primeor-solutions-data-analytics-internship](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
