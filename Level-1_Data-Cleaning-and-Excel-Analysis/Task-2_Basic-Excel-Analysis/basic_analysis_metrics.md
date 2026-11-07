# Level 1 Task 2: Basic Excel Analysis Report

**Company:** Primeor Solutions  
**Project:** E-Commerce Data Analytics Internship  
**Author:** Rishi Prajapati  
**Workbook:** `Level-1_Data-Cleaning-and-Excel-Analysis/Ecommerce_Analysis_Level1.xlsx` (Sheet: `Basic Excel Analysis`)

---

## 1. Executive Summary KPIs

The basic analysis was conducted on the cleaned global e-commerce dataset (51,271 records) across global sales from 2011 to 2014. The calculations below are embedded directly as native Excel formulas (`SUM`, `AVERAGE`) referencing the raw clean data table.

| Metric | Excel Formula | Value | Business Takeaway |
| :--- | :--- | :--- | :--- |
| **Total Sales** | `=SUM('Cleaned Dataset'!O2:O51272)` | **\$12,635,222.00** | Strong top-line revenue generated across 13 geographic regions. |
| **Total Profit** | `=SUM('Cleaned Dataset'!R2:R51272)` | **\$1,467,721.69** | Overall profit margin stands at **11.62%**. |
| **Average Discount** | `=AVERAGE('Cleaned Dataset'!Q2:Q51272)` | **14.29%** | Moderate discounting strategy maintaining healthy transaction margins. |

---

## 2. Product Performance Analysis

### Top 5 Products by Sales (Revenue Drivers)
These 5 products are the highest revenue-generating offerings in the catalog, heavily dominated by enterprise telecommunications and high-end office machinery.

| Rank | Product Name | Category | Total Sales ($) |
| :---: | :--- | :--- | :---: |
| **1** | Apple Smart Phone, Full Size | Technology | \$86,936.00 |
| **2** | Cisco Smart Phone, Full Size | Technology | \$76,441.00 |
| **3** | Motorola Smart Phone, Full Size | Technology | \$73,159.00 |
| **4** | Nokia Smart Phone, Full Size | Technology | \$71,904.00 |
| **5** | Canon imageCLASS 2200 Advanced Copier | Technology | \$61,600.00 |

### Top 5 Loss-Making Products (Margin Drainers)
These products generated significant net negative profit, primarily driven by excessive discounting and high return/shipping overheads.

| Rank | Product Name | Category | Total Net Loss ($) |
| :---: | :--- | :--- | :---: |
| **1** | Cubify CubeX 3D Printer Double Head Print | Technology | -\$8,879.97 |
| **2** | Lexmark MX611dhe Monochrome Laser Printer | Technology | -\$4,589.97 |
| **3** | Motorola Smart Phone, Cordless | Technology | -\$4,447.04 |
| **4** | Cubify CubeX 3D Printer Triple Head Print | Technology | -\$3,839.99 |
| **5** | Bevis Round Table, Adjustable Height | Furniture | -\$3,649.89 |

> **Key Observation:** 3D Printers and specialized office hardware suffered from substantial margin deterioration, suggesting the need for revised pricing floors and discount thresholds.

---

## 3. Region-wise Sales Distribution

The global sales footprint spans across 13 major geographic territories:

| Rank | Region | Total Sales ($) | Sales Contribution (%) |
| :---: | :--- | :---: | :---: |
| 1 | **Central** | \$2,821,740.00 | 22.33% |
| 2 | **South** | \$1,600,600.00 | 12.67% |
| 3 | **North** | \$1,248,121.00 | 9.88% |
| 4 | **Oceania** | \$1,098,253.00 | 8.69% |
| 5 | **Southeast Asia** | \$883,702.00 | 6.99% |
| 6 | **North Asia** | \$846,991.00 | 6.70% |
| 7 | **EMEA** | \$805,053.00 | 6.37% |
| 8 | **Africa** | \$783,345.00 | 6.20% |
| 9 | **Central Asia** | \$752,839.00 | 5.96% |
| 10 | **West** | \$725,514.00 | 5.74% |
| 11 | **East** | \$678,548.00 | 5.37% |
| 12 | **Caribbean** | \$323,584.00 | 2.56% |
| 13 | **Canada** | \$66,932.00 | 0.53% |
| **Total** | **All Regions** | **\$12,635,222.00** | **100.00%** |
