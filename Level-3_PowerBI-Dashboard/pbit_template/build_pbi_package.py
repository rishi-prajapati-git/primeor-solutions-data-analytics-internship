import zipfile
import json
import os

def build_pbit():
    pbit_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Ecommerce_Analysis_Level3.pbit"))
    pbix_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Ecommerce_Analysis_Level3.pbix"))
    theme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Task-2_Dashboard-Features-and-Theme/Primeor_Executive_Theme.json"))
    
    with open(theme_path, 'r') as tf:
        theme_json = json.load(tf)
        
    layout_data = {
        "id": 1,
        "resourcePackages": [
            {
                "resourcePackage": {
                    "name": "SharedResources",
                    "type": 2,
                    "items": [
                        {
                            "name": "BaseThemes/PrimeorExecutiveTheme.json",
                            "path": "BaseThemes/PrimeorExecutiveTheme.json",
                            "type": 201
                        }
                    ]
                }
            }
        ],
        "sections": [
            {
                "id": 0,
                "name": "Section_Page1_ExecutiveOverview",
                "displayName": "Page 1 - Executive Overview",
                "filters": "[]",
                "ordinal": 0,
                "visualContainers": [
                    {"id": 1, "config": json.dumps({"name": "kpi_sales", "title": "Total Sales"})},
                    {"id": 2, "config": json.dumps({"name": "kpi_profit", "title": "Total Profit"})},
                    {"id": 3, "config": json.dumps({"name": "kpi_orders", "title": "Total Orders"})},
                    {"id": 4, "config": json.dumps({"name": "kpi_discount", "title": "Average Discount"})},
                    {"id": 5, "config": json.dumps({"name": "chart_market_rev", "title": "Market Revenue Performance"})},
                    {"id": 6, "config": json.dumps({"name": "donut_category", "title": "Sales Share by Category"})}
                ]
            },
            {
                "id": 1,
                "name": "Section_Page2_SalesAnalysis",
                "displayName": "Page 2 - Sales Analysis",
                "filters": "[]",
                "ordinal": 1,
                "visualContainers": [
                    {"id": 7, "config": json.dumps({"name": "bar_region_sales", "title": "Sales by Region"})},
                    {"id": 8, "config": json.dumps({"name": "bar_market_sales", "title": "Sales by Market"})},
                    {"id": 9, "config": json.dumps({"name": "trend_monthly_sales", "title": "Monthly Sales Trend"})},
                    {"id": 10, "config": json.dumps({"name": "perf_category", "title": "Category Performance"})}
                ]
            },
            {
                "id": 2,
                "name": "Section_Page3_ProductCustomerInsights",
                "displayName": "Page 3 - Product & Customer Insights",
                "filters": "[]",
                "ordinal": 2,
                "visualContainers": [
                    {"id": 11, "config": json.dumps({"name": "top_products", "title": "Top Products"})},
                    {"id": 12, "config": json.dumps({"name": "top_customers", "title": "Top Customers"})},
                    {"id": 13, "config": json.dumps({"name": "profit_subcat", "title": "Profit by Sub-Category"})},
                    {"id": 14, "config": json.dumps({"name": "segment_analysis", "title": "Segment Analysis"})}
                ]
            }
        ],
        "config": json.dumps({"theme": "Primeor Executive Theme", "version": "5.50"})
    }
    
    version_str = "2.128.1380.0 (24.04)"
    
    for target_file in [pbit_path, pbix_path]:
        with zipfile.ZipFile(target_file, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr("Version", version_str.encode('utf-16le'))
            z.writestr("[Content_Types].xml", """<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="json" ContentType="application/json"/><Default Extension="xml" ContentType="application/xml"/></Types>""")
            z.writestr("Layout", json.dumps(layout_data, indent=2).encode('utf-16le'))
            z.writestr("Settings", json.dumps({"version": "1.0", "settings": {"hideVisualHeader": False}}).encode('utf-16le'))
            z.writestr("Report/StaticResources/SharedResources/BaseThemes/PrimeorExecutiveTheme.json", json.dumps(theme_json, indent=2).encode('utf-8'))
            
        print(f"Created Power BI package: {target_file}")

if __name__ == '__main__':
    build_pbit()
