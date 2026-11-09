# Level 3 - Task 1: Interactive Power BI Dashboard Pages Architecture

**Organization:** Primeor Solutions — Data Analytics Internship  
**Project:** Global E-Commerce Data Analytics  
**Level:** Level 3 — Task 1: Dashboard Pages Development  
**Author:** Rishi Prajapati  
**Dataset Scale:** 51,271 records (2011 – 2014)

---

## 📌 Executive Overview
Task 1 focuses on designing and structuring a high-impact, 3-page interactive Power BI dashboard directly derived from the cleaned dataset (`cleaned_ecommerce_dataset.csv`). Each page addresses specific management tiers—from high-level C-suite KPIs to granular product and account performance.

---

## 🖥️ Page 1: Executive Overview

### Core Target Audience
Chief Executive Officer (CEO), Chief Commercial Officer (CCO), and Operations Leadership.

### Visual Components & Data Bindings
```
+---------------------------------------------------------------------------------------------------+
|  [KPI CARD 1]          |  [KPI CARD 2]          |  [KPI CARD 3]          |  [KPI CARD 4]          |
|  Total Sales: $12.64M  |  Total Profit: $1.47M  |  Total Orders: 51,271  |  Avg Discount: 14.29%  |
+---------------------------------------------------------------------------------------------------+
|  [BAR CHART]                                    |  [DONUT CHART]                                  |
|  Market Revenue Performance (APAC & EU Leading) |  Sales Share by Product Category                |
+---------------------------------------------------------------------------------------------------+
|  [CLUSTERED COLUMN CHART]                       |  [DONUT / GAUGE]                                |
|  Annual Growth Trajectory (YoY 2011 - 2014)     |  Segment Contribution (Consumer, Corp, Home)    |
+---------------------------------------------------------------------------------------------------+
```

1. **KPI Card 1 — Total Sales:**
   - **Measure:** `[Total Sales] = SUM(ecommerce_orders[sales])`
   - **Result:** **$12,635,222.00**
2. **KPI Card 2 — Total Profit:**
   - **Measure:** `[Total Profit] = SUM(ecommerce_orders[profit])`
   - **Result:** **$1,467,721.69** (Margin: 11.62%)
3. **KPI Card 3 — Total Orders:**
   - **Measure:** `[Total Orders] = DISTINCTCOUNT(ecommerce_orders[order_id])`
   - **Result:** **51,271**
4. **KPI Card 4 — Average Discount:**
   - **Measure:** `[Average Discount] = AVERAGE(ecommerce_orders[discount])`
   - **Result:** **14.29%**
5. **Market Revenue Horizontal Bar Chart:**
   - **X-Axis:** `[Total Sales]`
   - **Y-Axis:** `ecommerce_orders[market]`
   - **Takeaway:** APAC ($3.58M) and EU ($2.94M) represent 51.6% of enterprise sales.
6. **Product Category Sales Donut Chart:**
   - **Legend:** `ecommerce_orders[category]`
   - **Values:** `[Total Sales]`
   - **Share:** Technology (37.5%), Furniture (32.5%), Office Supplies (30.0%).
7. **Annual Growth Clustered Column Chart:**
   - **X-Axis:** `ecommerce_orders[year]`
   - **Values:** `[Total Sales]`, `[Total Profit]`
   - **Insight:** Consistent revenue growth from $2.26M (2011) to $4.30M (2014).

---

## 📈 Page 2: Sales Analysis

### Core Target Audience
VP of Sales, Regional Sales Directors, and Commercial Planning Teams.

### Visual Components & Data Bindings
```
+---------------------------------------------------------------------------------------------------+
|  [HORIZONTAL BAR CHART]                         |  [COLUMN CHART]                                 |
|  Sales by Global Region (13 Regions)            |  Market Revenue Breakdown ($ Millions)          |
+---------------------------------------------------------------------------------------------------+
|  [AREA / LINE TREND CHART]                      |  [CLUSTERED BAR CHART]                          |
|  Monthly Sales Trend (48-Month Chronology)      |  Category Performance (Sales vs Net Profit)     |
+---------------------------------------------------------------------------------------------------+
```

1. **Sales by Global Region:**
   - **Y-Axis:** `ecommerce_orders[region]`
   - **X-Axis:** `[Total Sales]`
   - **Finding:** Central ($2.82M), South ($1.60M), and North ($1.25M) dominate aggregate transaction volumes.
2. **Sales by Market:**
   - **X-Axis:** `ecommerce_orders[market]`
   - **Y-Axis:** `[Total Sales]`
   - **Finding:** Strong commercial penetration in APAC, EU, US, and LATAM.
3. **Monthly Sales Trend (48 Months):**
   - **X-Axis:** `ecommerce_orders[order_date]` (Hierarchy: Year > Month)
   - **Y-Axis:** `[Total Sales]`
   - **Pattern:** Highly recurring seasonal surge in Q4 (September – December).
4. **Category Performance (Sales vs. Profit):**
   - **X-Axis:** `ecommerce_orders[category]`
   - **Values:** `[Total Sales]`, `[Total Profit]`
   - **Finding:** Furniture lags in operating margin (6.97%) compared to Technology (13.98%).

---

## 🔍 Page 3: Product & Customer Insights

### Core Target Audience
Merchandising Category Managers, Key Account Executives, and Supply Chain Planners.

### Visual Components & Data Bindings
```
+---------------------------------------------------------------------------------------------------+
|  [TOP 10 BAR CHART]                             |  [TOP 10 BAR CHART]                             |
|  Top 10 Products by Sales Revenue               |  Top 10 Customers by Lifetime Sales             |
+---------------------------------------------------------------------------------------------------+
|  [DIVERGING HORIZONTAL BAR CHART]               |  [CLUSTERED COLUMN CHART]                       |
|  Profit by Sub-Category (Loss Highlights)       |  Segment Analysis (Sales vs Profit by Segment)  |
+---------------------------------------------------------------------------------------------------+
```

1. **Top 10 Products by Sales:**
   - **Y-Axis:** `ecommerce_orders[product_name]` (Top 10 Filter by `[Total Sales]`)
   - **X-Axis:** `[Total Sales]`
   - **Key Items:** Apple Smart Phone, Cisco Smart Phone, Canon imageCLASS Copier.
2. **Top 10 Customers by Sales:**
   - **Y-Axis:** `ecommerce_orders[customer_name]` (Top 10 Filter by `[Total Sales]`)
   - **X-Axis:** `[Total Sales]`
   - **Key Accounts:** Tom Ashbrook ($40.5k), Tamara Chand ($37.5k), Greg Tran ($35.6k).
3. **Profit by Sub-Category (Diverging Color Scale):**
   - **Y-Axis:** `ecommerce_orders[sub_category]`
   - **X-Axis:** `[Total Profit]`
   - **Color Formatting:** Red for profit < $0, Green for profit >= $0.
   - **Critical Hazard:** Tables incurred **-$64,113.55 in net losses**.
4. **Customer Segment Analysis:**
   - **X-Axis:** `ecommerce_orders[segment]`
   - **Values:** `[Total Sales]`, `[Total Profit]`
   - **Breakdown:** Consumer (51.5% sales, $749k profit), Corporate (30.3% sales, $441k profit), Home Office (18.2% sales, $277k profit).
