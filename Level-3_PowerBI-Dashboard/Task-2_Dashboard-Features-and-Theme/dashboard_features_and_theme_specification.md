# Level 3 - Task 2: Dashboard Features, Slicers, Formatting & Executive Theme

**Organization:** Primeor Solutions — Data Analytics Internship  
**Project:** Global E-Commerce Data Analytics  
**Level:** Level 3 — Task 2: Advanced Dashboard Features  
**Author:** Rishi Prajapati  
**Dataset Scale:** 51,271 records (2011 – 2014)

---

## 📌 Executive Summary
Task 2 focuses on delivering production-grade interactive dashboard features, unified executive styling, consistent typography, dynamic filtering (slicers), and responsive visual hierarchy to satisfy all internship presentation requirements.

---

## 🎨 1. Consistent Color Theme & Palette

The dashboard is built on the **Primeor Executive Midnight Theme** (`Primeor_Executive_Theme.json`):

| Role | Color Hex | Visual Usage | Business Intent |
| :--- | :--- | :--- | :--- |
| **Canvas Background** | `#0B132B` | Full page background | Deep midnight slate providing high contrast |
| **Card Container** | `#1C2541` | Visual tile background | Elevated card design with 8px corner radiuses |
| **Primary Accent** | `#3A86FF` | Sales revenue, bar charts, primary cards | Corporate electric blue symbolizing revenue |
| **Success / Profit** | `#06D6A0` | Net profit metrics, positive trends | Emerald green indicating positive margin |
| **Warning / Volume** | `#FFB703` | Total order volume, secondary series | Radiant amber highlighting operational load |
| **Risk / Negative** | `#EF476F` | Discounts, loss-making sub-categories | Coral red alerting leadership to bleeding tables |
| **Segment Violet** | `#7209B7` | Product charts & consumer segments | Regal purple distinguishing category assortment |
| **Primary Text** | `#FFFFFF` | Metric values, titles, active labels | Crisp pure white for effortless readability |
| **Secondary Text** | `#8D99AE` | Subtitles, axis tick marks, gridlines | Soft platinum gray eliminating visual fatigue |

---

## 🎛️ 2. Slicers & Global Filter Panes

Each of the 3 dashboard pages includes standardized, synchronized slicers located in a dedicated top/left filter pane:

1. **Year Slicer (Horizontal Tile / Dropdown):**
   - **Field:** `ecommerce_orders[year]`
   - **Selections:** `[2011]`, `[2012]`, `[2013]`, `[2014]`, or `[Select All]`
   - **Interaction:** Synchronized across all pages to evaluate annual performance evolution.
2. **Global Market Slicer (Dropdown):**
   - **Field:** `ecommerce_orders[market]`
   - **Options:** APAC, EU, US, LATAM, EMEA, Africa, Canada.
   - **Interaction:** Allows regional VP reviews on a single click.
3. **Product Category Slicer (Tile / Buttons):**
   - **Field:** `ecommerce_orders[category]`
   - **Options:** Technology, Furniture, Office Supplies.
4. **Customer Segment Slicer:**
   - **Field:** `ecommerce_orders[segment]`
   - **Options:** Consumer, Corporate, Home Office.

---

## 📊 3. Interactive Visuals & Cross-Filtering Mechanics

- **Cross-Filtering & Cross-Highlighting:**
  Clicking on the `Furniture` wedge on Page 1 dynamically filters the `Market Revenue` chart and immediately highlights the margin compression in `Tables` on Page 3.
- **Drill-Through Capabilities:**
  Right-clicking any region on Page 2 allows users to drill through to a granular Country and State breakdown.
- **Hierarchical Date Trend:**
  The `Monthly Sales Trend` chart supports expanding from **Year > Quarter > Month**, enabling drill-down into specific Q4 surges.
- **Custom Tooltips:**
  Hovering over any product or customer visual displays contextual tooltip cards featuring:
  - Total Revenue ($)
  - Net Profit ($)
  - Units Sold
  - Profit Margin %
  - Average Discount Applied

---

## 📋 4. Final Submission Deliverables Check

As mandated by page 14 of the project brief:
- [x] **Cleaned Dataset:** `dataset/cleaned/cleaned_ecommerce_dataset.csv`
- [x] **SQL Queries File:** `Level-2_SQL-Data-Analysis/Task-2_SQL-Queries/all_level2_queries.sql`
- [x] **Excel Analysis File:** `Level-1_Data-Cleaning-and-Excel-Analysis/Ecommerce_Analysis_Level1.xlsx`
- [x] **Power BI Dashboard:** `Level-3_PowerBI-Dashboard/Ecommerce_Analysis_Level3.pbix` (and `.pbit`)
- [x] **Final Business Insights Reports (PDF):**
  - Level 2 SQL Insights: `Level-2_SQL-Data-Analysis/Task-3_SQL-Insights-Report/Level2_SQL_Business_Insights_Report.pdf`
  - Level 3 Power BI Dashboard: `Level-3_PowerBI-Dashboard/Task-2_Dashboard-Features-and-Theme/Level3_PowerBI_Dashboard_Report.pdf`
