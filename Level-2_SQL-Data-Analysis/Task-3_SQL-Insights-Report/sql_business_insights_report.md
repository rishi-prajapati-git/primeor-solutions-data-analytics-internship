# Level 2 - Task 3: SQL Business Insights Report

**Company:** Primeor Solutions — Data Analytics Internship  
**Project:** Global E-Commerce Data Analytics  
**Level:** Level 2 — SQL Data Analysis  
**Analyst:** Rishi Prajapati  
**Dataset Scale:** 51,271 records (2011 – 2014)

---

## Executive Summary

Through relational SQL querying and quantitative analysis across 51,271 global transactions, this report synthesizes the core findings requested by the project requirements. The findings provide senior leadership with clear insights into revenue concentration, margin erosion, fulfillment distribution, and strategic intervention opportunities.

---

## 1. Core Evaluation Questions (From Internship Brief)

### Q1: Which market generates the highest revenue?
- **Finding:** **APAC (Asia-Pacific)** is the company's largest and most lucrative market, generating **$3,581,785.00** in total revenue, representing **28.35%** of global sales and producing **$437,023.52** in net profit (12.20% margin).
- **Ranking of All Global Markets:**
  1. **APAC:** $3,581,785.00 (28.35% revenue share, $437.0k profit)
  2. **EU (European Union):** $2,937,166.00 (23.25% revenue share, $372.9k profit)
  3. **US (United States):** $2,297,022.00 (18.18% revenue share, $286.0k profit)
  4. **LATAM (Latin America):** $2,163,919.00 (17.13% revenue share, $221.3k profit)
  5. **EMEA (Europe, Middle East, Africa):** $805,053.00 (6.37% revenue share, $43.8k profit)
  6. **Africa:** $783,345.00 (6.20% revenue share, $88.9k profit)
  7. **Canada:** $66,932.00 (0.53% revenue share, $17.8k profit — highest profit margin at 26.56%)

### Q2: Which categories are least profitable?
- **Category Level:**
  - **Furniture** is the least profitable category overall. It generates **$4,105,771.00** in revenue (32.49% of sales) but yields only **$286,164.92** in profit, resulting in a net profit margin of only **6.97%** and an average profit per order of only **$29.00**.
  - In comparison, **Technology** delivers a **13.98% margin** ($65.44 profit/order) and **Office Supplies** delivers a **13.69% margin**.
- **Sub-Category Level (Critical Hazard):**
  - **Tables (Furniture)** is the single worst performer across the entire enterprise, generating **-$64,113.55 in net losses** on $757,042.00 of sales (-8.48% margin).
  - Heavy loss-making occurs due to steep discounting (>35%) coupled with high freight and bulky product handling costs.

### Q3: Which shipping mode is most commonly used?
- **Finding:** **Standard Class** is overwhelmingly the most preferred fulfillment method, capturing **60.00%** of all orders (30,764 orders).
- **Full Ship Mode Breakdown:**
  1. **Standard Class:** 30,764 orders (60.00% share, $7.57M sales, $19.96 avg shipping cost)
  2. **Second Class:** 10,304 orders (20.10% share, $2.56M sales, $30.44 avg shipping cost)
  3. **First Class:** 7,504 orders (14.64% share, $1.83M sales, $41.04 avg shipping cost)
  4. **Same Day:** 2,699 orders (5.26% share, $667.1k sales, $42.96 avg shipping cost)

---

## 2. In-Depth SQL Analytical Insights

```
+-----------------------------------------------------------------------------------------+
|                                    KEY INSIGHTS DASHBOARD                               |
+-----------------------------------------------------------------------------------------+
| Total Sales:         $12,635,222.00   | Total Net Profit:          $1,467,721.69        |
| Total Orders:        51,271           | Unprofitable Orders:       12,534 (24.45%)      |
| Top Revenue Market:  APAC (28.35%)    | Cumulative Loss Amount:    -$518,633.91         |
| Most Profitable Cat: Technology ($663k)| High Discount Category:    Furniture (16.80%)   |
+-----------------------------------------------------------------------------------------+
```

### Insight 1: The Root Cause of Bleeding Orders (Negative Profit Analysis)
- SQL querying revealed that **12,534 orders (24.45%)** were executed at a net financial loss, eroding **$518,633.91** from company gross earnings.
- While profitable orders maintained an average discount rate of **4.38%**, loss-making orders carried an average discount of **45.08%**.
- Across orders with discounts > 40%, the loss incidence exceeded **82%**, confirming that promotional margin discounting is improperly calibrated against logistics freight charges.

### Insight 2: Customer Account Profiling & The "Unprofitable Whale" Paradox
- The top revenue customer, **Tom Ashbrook**, generated $40,489.00 in revenue and $6,312.01 in profit across 30 orders.
- In contrast, the #5 customer by sales, **Sean Miller**, bought $35,131.00 in goods across 27 orders but generated a **loss of -$397.21**.
- This indicates that high-grossing VIP clients frequently negotiate volume discounts that wipe out transactional unit economics.

### Insight 3: Seasonality & Demand Surges
- Monthly time-series SQL aggregation demonstrates pronounced Q4 surges every single calendar year:
  - January - February typically represent the annual lows ($90k - $140k/month).
  - September through December experience dramatic volume increases, reaching peaks exceeding $400k+/month and peaking at $500k+ in late 2014.
  - Fulfillment capacity, inventory restocking, and carrier contracts should align dynamically with this Q4 cadence.

### Insight 4: Category & Sub-Category Product Portfolios
- **Technology (The Cash Cow):** Generates $4.74M in revenue and $663.3k in profit. Top driver is **Copiers** ($258.2k profit, 17.12% margin) and **Phones** ($216.8k profit).
- **Office Supplies (The Volume Driver):** Comprises 60.98% of total order count (31,267 orders) with dependable margins (13.69%).
- **Furniture (The Strategic Challenge):** Despite chairs and bookcases generating profits, Tables heavily drag down performance (-$64.1k loss).

---

## 3. Strategic Business Recommendations

1. **Implement Dynamic Discount Caps:**  
   Cap frontline discounting on Furniture (especially Tables) at **15% maximum**. Eliminate automatic tier discounting when freight distance is high.
2. **Revise Enterprise Pricing for Bulk Buyers:**  
   Implement minimum margin floors (e.g., minimum 8% net margin) for high-volume accounts to prevent accounts like Sean Miller from eroding profit.
3. **Double Down on APAC & EU Core Expansion:**  
   APAC and EU together account for **51.60%** of global turnover and generate over **$809k** in net profit. Further marketing investment in these territories will yield optimal returns.
4. **Logistics Optimization for Standard Class:**  
   Since 60% of all orders use Standard Class, negotiate bulk zone-skipping and volume freight contracts with postal partners to reduce the $19.96 average delivery cost.
