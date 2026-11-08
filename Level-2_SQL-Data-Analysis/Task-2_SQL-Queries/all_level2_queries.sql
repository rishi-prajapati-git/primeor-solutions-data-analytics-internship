-- ====================================================================
-- Primeor Solutions Data Analytics Internship
-- Level 2: Task 2 - SQL Queries for Business Analytics
-- Database: ecommerce_orders (MySQL / PostgreSQL / SQLite Compatible)
-- Total Records: 51,271
-- ====================================================================

-- --------------------------------------------------------------------
-- Query 1: Top 10 Profitable Products
-- Business Value: Identify core high-margin product offerings that drive 
--                 the organization's profitability.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 2: Top 10 Customers by Sales
-- Business Value: Surface high-value enterprise and individual accounts 
--                 for loyalty and key account management.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 3: Region-Wise Total Sales
-- Business Value: Geographic revenue distribution and market penetration
--                 benchmarking across regions.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 4: Category-Wise Average Profit
-- Business Value: Evaluate operating efficiency and product margins across 
--                 high-level product categories.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 5: Highest Discount Category
-- Business Value: Assess discount exposure and detect if discounting strategies
--                 are diluting profitability.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 6: Orders with Negative Profit (Loss-Making Orders Analysis)
-- Business Value: Quantify bleeding transactions to diagnose root causes
--                 such as excessive discounting or high shipping overhead.
-- --------------------------------------------------------------------
-- Overview summary of negative profit transactions:
SELECT 
    COUNT(*) AS total_loss_orders,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_orders)), 2) AS loss_order_pct,
    ROUND(SUM(profit), 2) AS total_net_loss,
    ROUND(AVG(profit), 2) AS avg_loss_amount,
    ROUND(AVG(discount) * 100, 2) AS avg_discount_on_losses,
    ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost_on_losses
FROM ecommerce_orders
WHERE profit < 0;

-- Top 10 worst loss-making transactions:
SELECT 
    order_id,
    order_date,
    customer_name,
    country,
    product_name,
    category,
    sub_category,
    ROUND(sales, 2) AS sales,
    discount,
    ROUND(profit, 2) AS profit,
    shipping_cost
FROM ecommerce_orders
WHERE profit < 0
ORDER BY profit ASC
LIMIT 10;


-- --------------------------------------------------------------------
-- Query 7: Monthly Sales Trend
-- Business Value: Time-series analysis of sales volume and profits to detect
--                 seasonality, growth trajectory, and Q4 surges.
-- --------------------------------------------------------------------
SELECT 
    SUBSTR(order_date, 1, 7) AS order_year_month,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales), 2) AS monthly_sales,
    ROUND(SUM(profit), 2) AS monthly_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS monthly_margin_pct
FROM ecommerce_orders
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY order_year_month ASC;


-- --------------------------------------------------------------------
-- Query 8: Market-Wise Revenue Analysis
-- Business Value: Evaluate international market share, strategic revenue
--                 generation, and regional margin health.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 9: Top-Performing Sub-Categories
-- Business Value: Product line breakdown by revenue, profitability, and
--                 margin health to optimize catalogue assortment.
-- --------------------------------------------------------------------
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


-- --------------------------------------------------------------------
-- Query 10: Ship Mode Usage Analysis
-- Business Value: Fulfillment logistics analysis comparing customer shipping
--                 preferences, operational load, and cost impact.
-- --------------------------------------------------------------------
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
