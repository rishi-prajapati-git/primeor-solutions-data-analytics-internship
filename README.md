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

## 📦 Submission ZIP Folder Architecture

All required project deliverables have been organized into the official submission archive:  
**`Primeor_Solutions_Final_Project_Submission_Rishi_Prajapati.zip`** (10.39 MB).

When unzipped, the project directory follows this clean, categorized structure:

```text
Primeor_Solutions_Project_Rishi_Prajapati/
│
├── 1_Cleaned_Dataset/
│   └── cleaned_ecommerce_dataset.csv                   # 51,271 normalized rows, 0 nulls, 0 duplicates
│
├── 2_Excel_Analysis/
│   └── Ecommerce_Analysis_Level1.xlsx                  # KPI formulas, Pivot tables & embedded charts
│
├── 3_SQL_Queries/
│   ├── all_level2_queries.sql                          # 10 production SQL business analytical queries
│   └── sql_query_results.xlsx                          # 10-sheet structured Excel workbook with query outputs
│
├── 4_PowerBI_Dashboard/
│   ├── Ecommerce_Analysis_Level3.pbix                  # Official standalone Power BI report package
│   └── Ecommerce_Analysis_Level3.pbit                  # Power BI report template with pre-configured schema
│
├── 5_Final_Business_Insights_Report/
│   ├── Level2_SQL_Business_Insights_Report.pdf         # Executive SQL insights report with recommendations
│   └── Level3_PowerBI_Dashboard_Report.pdf             # 3-Page Executive Power BI presentation report
│
├── 6_Project_Presentation/
│   └── Rishi_Prajapati_Primeor_Intelligence_Presentation.pptx # Comprehensive 6-slide internship presentation
│
└── 7_Documentation_and_Launcher/
    ├── README.md                                       # Complete project documentation & guide
    └── run_dashboard.bat                               # One-click interactive dashboard launcher
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

Evaluators and reviewers have **four seamless options** to explore and verify this project:

### Method 1: One-Click Desktop Launcher (Recommended ⚡)
If you are evaluating from the unzipped submission folder:
- Open the **`7_Documentation_and_Launcher/`** folder.
- Double-click **`run_dashboard.bat`** (or run `run_dashboard.bat` from the root of the repository).
- Required dependencies will be verified automatically, and the interactive web dashboard will launch in your default browser at `http://localhost:8501`.

---

### Method 2: Terminal / Command Prompt Execution
Execute the following commands in any terminal (Command Prompt, PowerShell, or Bash):

```bash
# 1. Install required dependencies
pip install pandas plotly streamlit openpyxl reportlab

# 2. Launch the interactive dashboard application
python -m streamlit run "Level-3_PowerBI-Dashboard/app.py"
```
The browser will automatically open the interactive dashboard with dynamic multi-market slicers and visual analytics at `http://localhost:8501`.

---

### Method 3: Power BI Desktop File (.pbix)
For evaluators with **Power BI Desktop** installed:
1. Locate the report file: **`4_PowerBI_Dashboard/Ecommerce_Analysis_Level3.pbix`** (or in `Level-3_PowerBI-Dashboard/Ecommerce_Analysis_Level3.pbix`).
2. Double-click to open in **Power BI Desktop**.
3. All three pages (`Page 1 - Executive Overview`, `Page 2 - Sales Analysis`, and `Page 3 - Product & Customer Insights`) are pre-built with DAX calculations and synchronized visual filters.

---

### Method 4: Zero-Setup Executive Presentation PDF
For instant evaluation without running software or scripts:
- Review the comprehensive presentation document: **`5_Final_Business_Insights_Report/Level3_PowerBI_Dashboard_Report.pdf`** (or in `Level-3_PowerBI-Dashboard/Task-2_Dashboard-Features-and-Theme/Level3_PowerBI_Dashboard_Report.pdf`) containing high-resolution renders, KPI models, and business recommendations.

---

## 📋 Final Submission Package Checklist

As required by the Primeor Solutions project guidelines:
- [x] **Cleaned Dataset:** `1_Cleaned_Dataset/cleaned_ecommerce_dataset.csv`
- [x] **SQL Queries File:** `3_SQL_Queries/all_level2_queries.sql`
- [x] **Excel Analysis File:** `2_Excel_Analysis/Ecommerce_Analysis_Level1.xlsx`
- [x] **Power BI Dashboard:** `4_PowerBI_Dashboard/Ecommerce_Analysis_Level3.pbix` (and `.pbit`)
- [x] **Final Business Insights Reports (PDF):**
  - SQL Insights: `5_Final_Business_Insights_Report/Level2_SQL_Business_Insights_Report.pdf`
  - Power BI Presentation: `5_Final_Business_Insights_Report/Level3_PowerBI_Dashboard_Report.pdf`
- [x] **Presentation Slides:** `6_Project_Presentation/Rishi_Prajapati_Primeor_Intelligence_Presentation.pptx`
- [x] **All Files Packaged in Single ZIP:** `Primeor_Solutions_Final_Project_Submission_Rishi_Prajapati.zip`

---

## 👤 Author & Contact
- **Rishi Prajapati**  
- **Role:** Data Analytics Intern  
- **Organization:** Primeor Solutions  
- **GitHub:** [@rishi-prajapati-git](https://github.com/rishi-prajapati-git)  
- **Repository:** [primeor-solutions-data-analytics-internship](https://github.com/rishi-prajapati-git/primeor-solutions-data-analytics-internship)
