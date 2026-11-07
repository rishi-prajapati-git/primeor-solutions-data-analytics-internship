# Level 1 Task 1: Data Understanding & Cleaning Report

**Company:** Primeor Solutions  
**Project:** E-Commerce Data Analytics Internship  
**Author:** Rishi Prajapati  
**Dataset:** Global E-Commerce Sales Dataset  

---

## 1. Overview & Objectives
The primary objective of Level 1 Task 1 is to prepare the raw e-commerce transaction dataset for accurate downstream analytics and business intelligence. Raw real-world datasets often suffer from inconsistencies, missing information, duplicate entries, and improper date and number formats.

### Operations Performed:
- **Duplicate Removal:** Identified and eliminated duplicate transaction rows to prevent inflation of financial totals.
- **Null & Missing Value Handling:** Strategically imputed missing customer identifiers and missing profit values without data loss.
- **Text Standardization:** Stripped leading/trailing spaces and harmonized text encoding.
- **Numerical Value Cleaning:** Cleaned formatted strings containing thousands separators (`,`) into standard decimal floats.
- **Date Format Standardization:** Converted varied delimiter date formats (mixed slashes `/` and hyphens `-`) into international standard ISO 8601 (`YYYY-MM-DD`).

---

## 2. Data Cleaning Summary Metrics

| Metric | Raw Dataset | Cleaned Dataset | Action Taken |
| :--- | :--- | :--- | :--- |
| **Total Rows** | 51,325 | 51,271 | 54 duplicate rows removed |
| **Total Columns** | 21 | 21 | All essential business attributes preserved |
| **Missing Customer Names** | 79 rows | 0 rows | Imputed with `"Unknown Customer"` |
| **Missing Profit Values** | 14 rows | 0 rows | Imputed using Sub-Category median profit |
| **Sales Format** | Object (String with commas) | Float64 | Sanitized string and converted to numeric float |
| **Order & Ship Date Format** | Inconsistent (`D/M/Y`, `DD-MM-YYYY`) | Standard ISO (`YYYY-MM-DD`) | Parsed via day-first datetime parser and formatted |
| **Trailing Whitespaces** | Present in `product_name` | Cleaned | Stripped all string features |

---

## 3. Dataset Schema (Cleaned)

| # | Column Name | Data Type | Description |
| :--- | :--- | :--- | :--- |
| 1 | `order_id` | String | Unique order identifier |
| 2 | `order_date` | Date (`YYYY-MM-DD`) | Date when the order was placed |
| 3 | `ship_date` | Date (`YYYY-MM-DD`) | Date when the order was shipped |
| 4 | `ship_mode` | String | Shipping tier (`Standard Class`, `Second Class`, `First Class`, `Same Day`) |
| 5 | `customer_name` | String | Customer full name |
| 6 | `segment` | String | Customer market segment (`Consumer`, `Corporate`, `Home Office`) |
| 7 | `state` | String | Destination state/province |
| 8 | `country` | String | Destination country |
| 9 | `market` | String | Global business market (`APAC`, `EU`, `US`, `LATAM`, `EMEA`, `Africa`, `Canada`) |
| 10 | `region` | String | Geographic sales region |
| 11 | `product_id` | String | Unique product catalog ID |
| 12 | `category` | String | Product super-category (`Technology`, `Furniture`, `Office Supplies`) |
| 13 | `sub_category` | String | Specific product sub-category (17 categories) |
| 14 | `product_name` | String | Full descriptive name of the item |
| 15 | `sales` | Float | Transaction revenue in USD |
| 16 | `quantity` | Integer | Units ordered |
| 17 | `discount` | Float | Rate of discount applied (0.00 to 0.85) |
| 18 | `profit` | Float | Net profit / loss from transaction in USD |
| 19 | `shipping_cost` | Float | Shipping and handling expense |
| 20 | `order_priority` | String | Order handling urgency (`Critical`, `High`, `Medium`, `Low`) |
| 21 | `year` | Integer | Order transaction year (2011 - 2014) |

---

## 4. Verification & Integrity Check
- **Zero Null Values:** Verification confirms 0 null entries across all 21 columns.
- **Data Fidelity:** Total clean records: **51,271** ready for Excel modeling, SQL ingestion, and Power BI visualization.
