import sqlite3
import pandas as pd
import os

def run_and_export():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ecommerce_analysis.db'))
    conn = sqlite3.connect(db_path)
    
    queries = {
        "1_top_10_profitable_products": """
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
        """,
        "2_top_10_customers_by_sales": """
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
        """,
        "3_region_wise_total_sales": """
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
        """,
        "4_category_wise_avg_profit": """
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
        """,
        "5_highest_discount_category": """
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
        """,
        "6_negative_profit_orders_summary": """
            SELECT 
                COUNT(*) AS total_loss_orders,
                ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_orders)), 2) AS loss_order_pct,
                ROUND(SUM(profit), 2) AS total_net_loss,
                ROUND(AVG(profit), 2) AS avg_loss_amount,
                ROUND(AVG(discount) * 100, 2) AS avg_discount_on_losses,
                ROUND(AVG(shipping_cost), 2) AS avg_shipping_cost_on_losses
            FROM ecommerce_orders
            WHERE profit < 0;
        """,
        "7_monthly_sales_trend": """
            SELECT 
                SUBSTR(order_date, 1, 7) AS order_year_month,
                COUNT(order_id) AS total_orders,
                ROUND(SUM(sales), 2) AS monthly_sales,
                ROUND(SUM(profit), 2) AS monthly_profit,
                ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS monthly_margin_pct
            FROM ecommerce_orders
            GROUP BY SUBSTR(order_date, 1, 7)
            ORDER BY order_year_month ASC;
        """,
        "8_market_wise_revenue": """
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
        """,
        "9_top_performing_sub_categories": """
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
        """,
        "10_ship_mode_usage": """
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
        """
    }
    
    excel_out = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sql_query_results.xlsx'))
    with pd.ExcelWriter(excel_out, engine='openpyxl') as writer:
        for name, sql in queries.items():
            df_res = pd.read_sql_query(sql, conn)
            sheet_title = name[:31] # Excel 31 char limit
            df_res.to_excel(writer, sheet_name=sheet_title, index=False)
            print(f"Exported {name} ({len(df_res)} rows)")
            
    conn.close()
    print(f"\nAll query results successfully saved to: {excel_out}")

if __name__ == '__main__':
    run_and_export()
