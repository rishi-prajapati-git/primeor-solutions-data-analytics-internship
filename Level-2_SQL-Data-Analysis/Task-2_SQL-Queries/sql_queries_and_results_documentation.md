# Level 2 - Task 2: SQL Queries for Business Analytics

This document contains the 10 core SQL queries executed on the database along with structured outputs, explanations, and key takeaways.

---

## 1. Top 10 Profitable Products
**Business Objective:** Identify the product offerings that deliver the largest cumulative profit.

```sql
SELECT 
    product_id,
    product_name,
    category,
    sub_category,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(sales), 2) AS total_sales,
    SUM(quantity) AS total_units_sold,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM ecommerce_orders
GROUP BY product_id, product_name, category, sub_category
ORDER BY total_profit DESC
LIMIT 10;
```

### Result Sample:
| Product ID | Product Name | Category | Sub-Category | Total Profit ($) | Total Sales ($) | Profit Margin (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TEC-CO-10004722` | Canon imageCLASS 2200 Advanced Copier | Technology | Copiers | 25,199.93 | 61,600.00 | 40.91% |
| `OFF-AP-10004512` | Cisco Smart Phone, Full Size | Technology | Phones | 8,248.80 | 21,148.00 | 39.01% |
| `TEC-PH-10004823` | Motorola Smart Phone, Full Size | Technology | Phones | 7,610.16 | 22,261.00 | 34.19% |
| `OFF-BI-10003527` | Fellowes PB500 Electric Punch Plastic Comb Binding | Office Supplies | Binders | 7,753.04 | 27,454.00 | 28.24% |
| `TEC-CO-10001449` | Hewlett Packard LaserJet 3310 Copier | Technology | Copiers | 6,983.88 | 18,840.00 | 37.07% |

---

## 2. Top 10 Customers by Sales
**Business Objective:** Identify the highest-spending customers for VIP retention and enterprise account management.

```sql
SELECT 
    customer_name,
    segment,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_units_bought,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(sales), 2) AS avg_order_value
FROM ecommerce_orders
GROUP BY customer_name, segment
ORDER BY total_sales DESC
LIMIT 10;
```

### Result Sample:
| Customer Name | Segment | Total Orders | Units Bought | Total Sales ($) | Total Profit ($) | Avg Order Value ($) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tom Ashbrook** | Home Office | 30 | 284 | $40,489.00 | $6,312.01 | $421.76 |
| **Tamara Chand** | Corporate | 36 | 271 | $37,453.00 | $8,672.89 | $334.40 |
| **Greg Tran** | Consumer | 34 | 310 | $35,552.00 | $5,214.12 | $351.01 |
| **Christopher Conant** | Consumer | 39 | 287 | $35,187.00 | $5,603.34 | $382.47 |
| **Sean Miller** | Home Office | 27 | 164 | $35,131.00 | -$397.21 | $408.50 |

> *Observation*: Customer Sean Miller generated $35k+ in sales but negative net profit (-$397.21) due to heavily discounted bulk purchases.

---

## 3. Region-Wise Total Sales
**Business Objective:** Evaluate global geographic distribution of revenue and order volume.

```sql
SELECT 
    region,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(sales) * 100.0 / (SELECT SUM(sales) FROM ecommerce_orders)), 2) AS sales_contribution_pct,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM ecommerce_orders
GROUP BY region
ORDER BY total_sales DESC;
```

### Top Regions:
1. **Central**: $2,821,740.00 (22.33% of total sales, $311,570.52 profit)
2. **South**: $1,600,600.00 (12.67% of total sales, $140,245.18 profit)
3. **North**: $1,248,121.00 (9.88% of total sales, $194,598.48 profit)
4. **Oceania**: $1,098,253.00 (8.69% of total sales, $121,515.23 profit)
5. **Southeast Asia**: $883,702.00 (6.99% of total sales, $17,653.46 profit — low margin of 2.00%)

---

## 4. Category-Wise Average Profit
**Business Objective:** Determine the average profitability per transaction across main categories.

```sql
SELECT 
    category,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(profit), 2) AS avg_profit_per_order,
    ROUND(AVG(sales), 2) AS avg_sales_per_order,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_pct,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM ecommerce_orders
GROUP BY category
ORDER BY avg_profit_per_order DESC;
```

### Results:
| Category | Total Orders | Total Sales ($) | Total Profit ($) | Avg Profit/Order ($) | Margin (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Technology** | 10,137 | $4,742,975.00 | $663,337.29 | **$65.44** | 13.98% |
| **Furniture** | 9,867 | $4,105,771.00 | $286,164.92 | **$29.00** | 6.97% |
| **Office Supplies** | 31,267 | $3,786,476.00 | $518,219.48 | **$16.57** | 13.69% |

---

## 5. Highest Discount Category
**Business Objective:** Identify which category incurs the highest discount levels.

```sql
SELECT 
    category,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_pct,
    ROUND(MAX(discount) * 100, 2) AS max_discount_pct,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM ecommerce_orders
GROUP BY category
ORDER BY avg_discount_pct DESC;
```

### Result:
- **Furniture** is the highest discounted category with an average discount of **16.80%**, which directly depresses its net profit margin to **6.97%**.
- Office Supplies averages 13.74% discount.
- Technology averages 13.54% discount.

---

## 6. Orders with Negative Profit
**Business Objective:** Quantify financial losses resulting from unprofitable sales.

```sql
SELECT 
    COUNT(*) AS total_loss_orders,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_orders)), 2) AS loss_order_pct,
    ROUND(SUM(profit), 2) AS total_net_loss,
    ROUND(AVG(profit), 2) AS avg_loss_amount,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_on_losses,
    ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost_on_losses
FROM ecommerce_orders
WHERE profit < 0;
```

### Key Metrics:
- **Total Unprofitable Orders:** 12,534 orders (24.45% of all orders)
- **Cumulative Loss Incurred:** **-$518,633.91**
- **Average Discount on Unprofitable Orders:** **45.08%** (compared to 14.29% dataset average)
- *Conclusion*: Deep discounting (>40%) is the single largest cause of negative profit orders.

---

## 7. Monthly Sales Trend
**Business Objective:** Detect recurring seasonality, peak demand periods, and multi-year growth.

```sql
SELECT 
    SUBSTR(order_date, 1, 7) AS order_year_month,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS monthly_margin_pct
FROM ecommerce_orders
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_year_month ASC;
```

*Summary Insights:* Strong recurring seasonal peak every year from **September through December**, with November/December consistently exceeding $400k+ in sales.

---

## 8. Market-Wise Revenue Analysis
**Business Objective:** Determine high-performing geographic market clusters.

```sql
SELECT 
    market,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(sales) * 100.0 / (SELECT SUM(sales) FROM ecommerce_orders)), 2) AS revenue_share_pct,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct,
    ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost
FROM ecommerce_orders
GROUP BY market
ORDER BY total_revenue DESC;
```

### Results:
| Market | Total Orders | Total Revenue ($) | Share (%) | Total Profit ($) | Margin (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **APAC** | 10,997 | $3,581,785.00 | **28.35%** | $437,023.52 | 12.20% |
| **EU** | 9,998 | $2,937,166.00 | **23.25%** | $372,889.59 | 12.70% |
| **US** | 9,990 | $2,297,022.00 | **18.18%** | $286,031.44 | 12.45% |
| **LATAM** | 10,291 | $2,163,919.00 | **17.13%** | $221,324.89 | 10.23% |
| **EMEA** | 5,026 | $805,053.00 | **6.37%** | $43,817.07 | 5.44% |
| **Africa** | 4,585 | $783,345.00 | **6.20%** | $88,855.41 | 11.34% |
| **Canada** | 384 | $66,932.00 | **0.53%** | $17,779.77 | **26.56%** |

---

## 9. Top-Performing Sub-Categories
**Business Objective:** Assortment level analysis by sales volume and profitability.

```sql
SELECT 
    sub_category,
    category,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_quantity_sold,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin_pct
FROM ecommerce_orders
GROUP BY sub_category, category
ORDER BY total_sales DESC
LIMIT 10;
```

### Top Sub-Categories:
1. **Phones** (Technology): $1,706,824.00 Sales | $216,750.89 Profit (12.70% Margin)
2. **Copiers** (Technology): $1,509,436.00 Sales | $258,174.43 Profit (17.12% Margin)
3. **Chairs** (Furniture): $1,501,682.00 Sales | $141,716.73 Profit (9.44% Margin)
4. **Bookcases** (Furniture): $1,466,572.00 Sales | $161,703.08 Profit (11.05% Margin)
5. **Storage** (Office Supplies): $1,126,826.00 Sales | $108,525.97 Profit (9.63% Margin)
6. *Warning*: **Tables** (Furniture) ranks #8 in sales ($757,042.00) but generated a heavy loss of **-$64,113.55** (-8.48% Margin).

---

## 10. Ship Mode Usage Analysis
**Business Objective:** Fulfillment breakdown and logistics cost analysis.

```sql
SELECT 
    ship_mode,
    COUNT(order_id) AS order_count,
    ROUND((COUNT(order_id) * 100.0 / (SELECT COUNT(*) FROM ecommerce_orders)), 2) AS usage_share_pct,
    ROUND(SUM(sales), 2) AS total_sales_volume,
    ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost,
    ROUND(SUM(shipping_cost), 2) AS total_shipping_cost
FROM ecommerce_orders
GROUP BY ship_mode
ORDER BY order_count DESC;
```

### Results:
| Ship Mode | Orders | Usage Share (%) | Sales Volume ($) | Avg Shipping Cost ($) | Total Shipping ($) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard Class** | 30,764 | **60.00%** | $7,574,395.00 | $19.96 | $614,049.40 |
| **Second Class** | 10,304 | **20.10%** | $2,563,078.00 | $30.44 | $313,654.56 |
| **First Class** | 7,504 | **14.64%** | $1,830,652.00 | $41.04 | $307,964.16 |
| **Same Day** | 2,699 | **5.26%** | $667,097.00 | $42.96 | $115,949.04 |
