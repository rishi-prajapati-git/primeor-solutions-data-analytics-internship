# Level 2 - Task 1: Import Data into SQL

## 1. Overview
The objective of this task is to import the cleaned e-commerce dataset (`cleaned_ecommerce_dataset.csv`, consisting of 51,271 records) into a relational database management system (RDBMS) to perform advanced SQL queries and analytics.

---

## 2. Table Schema Definition

The table schema `ecommerce_orders` was structured with appropriate data types and indexing:

| Column Name | SQL Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `VARCHAR(50)` | Unique order identifier |
| `order_date` | `DATE` | Date when the order was placed (`YYYY-MM-DD`) |
| `ship_date` | `DATE` | Date when the order was shipped (`YYYY-MM-DD`) |
| `ship_mode` | `VARCHAR(50)` | Shipping method (Standard Class, Second Class, etc.) |
| `customer_name` | `VARCHAR(100)` | Name of the customer |
| `segment` | `VARCHAR(50)` | Customer segment (Consumer, Corporate, Home Office) |
| `state` | `VARCHAR(100)` | State/Province |
| `country` | `VARCHAR(100)` | Destination country |
| `market` | `VARCHAR(50)` | Global market (APAC, EU, US, LATAM, EMEA, Africa, Canada) |
| `region` | `VARCHAR(50)` | Regional subdivision |
| `product_id` | `VARCHAR(50)` | Unique product identifier |
| `category` | `VARCHAR(50)` | Broad category (Technology, Furniture, Office Supplies) |
| `sub_category` | `VARCHAR(50)` | Product sub-category (Phones, Copiers, Chairs, etc.) |
| `product_name` | `VARCHAR(255)` | Full description/title of the product |
| `sales` | `DECIMAL(12, 2)` | Transaction revenue ($) |
| `quantity` | `INT` | Number of units purchased |
| `discount` | `DECIMAL(5, 4)` | Applied discount rate (e.g., 0.20 = 20%) |
| `profit` | `DECIMAL(12, 4)` | Net profit or loss ($) |
| `shipping_cost` | `DECIMAL(10, 2)` | Delivery cost charged/incurred ($) |
| `order_priority`| `VARCHAR(50)` | Priority level (Critical, High, Medium, Low) |
| `year` | `INT` | Order year (2011 - 2014) |

---

## 3. Implementation & Ingestion Methods

Three implementation methods have been provided:

1. **Portable SQLite Database (`ecommerce_analysis.db`)**:
   - Automated via `import_to_sqlite.py`.
   - Complete zero-config database included in repository for immediate replication without external server setup.
   - Verification count: **51,271 rows** successfully loaded.
2. **MySQL Script (`schema_and_setup.sql`)**:
   - DDL definitions with `LOAD DATA LOCAL INFILE` high-speed ingestion script.
   - Includes indexes for query performance (`idx_order_date`, `idx_customer_name`, `idx_category_sub`, `idx_region_market`).
3. **PostgreSQL Script (`schema_and_setup.sql`)**:
   - Compatible standard PostgreSQL table definition using `\copy` command.

---

## 4. Verification Check
- **Row count check**: `SELECT COUNT(*) FROM ecommerce_orders;` -> `51271`
- **Null values check on primary keys**: `SELECT COUNT(*) FROM ecommerce_orders WHERE order_id IS NULL OR product_id IS NULL;` -> `0`
- **Date range**: Orders span from `2011-01-01` to `2014-12-31` across all major global markets.
