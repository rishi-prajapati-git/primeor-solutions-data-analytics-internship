-- ====================================================================
-- Primeor Solutions Data Analytics Internship
-- Level 2: Task 1 - Database Schema & Data Ingestion Setup
-- File: schema_and_setup.sql
-- Description: DDL schema definitions and ingestion instructions for 
--              MySQL, PostgreSQL, and SQLite.
-- ====================================================================

-- --------------------------------------------------------------------
-- 1. MySQL DDL & IMPORT SCRIPT
-- --------------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS primeor_ecommerce_db;
USE primeor_ecommerce_db;

DROP TABLE IF EXISTS ecommerce_orders;

CREATE TABLE ecommerce_orders (
    order_id         VARCHAR(50) NOT NULL,
    order_date       DATE NOT NULL,
    ship_date        DATE NOT NULL,
    ship_mode        VARCHAR(50) NOT NULL,
    customer_name    VARCHAR(100) NOT NULL,
    segment          VARCHAR(50) NOT NULL,
    state            VARCHAR(100),
    country          VARCHAR(100) NOT NULL,
    market           VARCHAR(50) NOT NULL,
    region           VARCHAR(50) NOT NULL,
    product_id       VARCHAR(50) NOT NULL,
    category         VARCHAR(50) NOT NULL,
    sub_category     VARCHAR(50) NOT NULL,
    product_name     VARCHAR(255) NOT NULL,
    sales            DECIMAL(12, 2) NOT NULL,
    quantity         INT NOT NULL,
    discount         DECIMAL(5, 4) NOT NULL,
    profit           DECIMAL(12, 4) NOT NULL,
    shipping_cost    DECIMAL(10, 2) NOT NULL,
    order_priority   VARCHAR(50) NOT NULL,
    year             INT NOT NULL
);

-- Optimization Indexes
CREATE INDEX idx_order_date ON ecommerce_orders(order_date);
CREATE INDEX idx_customer_name ON ecommerce_orders(customer_name);
CREATE INDEX idx_category_sub ON ecommerce_orders(category, sub_category);
CREATE INDEX idx_region_market ON ecommerce_orders(region, market);

-- Fast CSV Import via MySQL LOAD DATA INFILE:
/*
LOAD DATA LOCAL INFILE 'C:/Users/praja/Downloads/Primeor Solutions Intern/dataset/cleaned/cleaned_ecommerce_dataset.csv'
INTO TABLE ecommerce_orders
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(order_id, order_date, ship_date, ship_mode, customer_name, segment, state, country, market, region, product_id, category, sub_category, product_name, sales, quantity, discount, profit, shipping_cost, order_priority, year);
*/

-- --------------------------------------------------------------------
-- 2. PostgreSQL DDL & IMPORT SCRIPT
-- --------------------------------------------------------------------
/*
CREATE TABLE ecommerce_orders (
    order_id         VARCHAR(50) NOT NULL,
    order_date       DATE NOT NULL,
    ship_date        DATE NOT NULL,
    ship_mode        VARCHAR(50) NOT NULL,
    customer_name    VARCHAR(100) NOT NULL,
    segment          VARCHAR(50) NOT NULL,
    state            VARCHAR(100),
    country          VARCHAR(100) NOT NULL,
    market           VARCHAR(50) NOT NULL,
    region           VARCHAR(50) NOT NULL,
    product_id       VARCHAR(50) NOT NULL,
    category         VARCHAR(50) NOT NULL,
    sub_category     VARCHAR(50) NOT NULL,
    product_name     VARCHAR(255) NOT NULL,
    sales            NUMERIC(12, 2) NOT NULL,
    quantity         INTEGER NOT NULL,
    discount         NUMERIC(5, 4) NOT NULL,
    profit           NUMERIC(12, 4) NOT NULL,
    shipping_cost    NUMERIC(10, 2) NOT NULL,
    order_priority   VARCHAR(50) NOT NULL,
    year             INTEGER NOT NULL
);

\copy ecommerce_orders FROM 'dataset/cleaned/cleaned_ecommerce_dataset.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
*/

-- --------------------------------------------------------------------
-- 3. SQLite DDL & CLI IMPORT
-- --------------------------------------------------------------------
/*
sqlite3 ecommerce_analysis.db
sqlite> .mode csv
sqlite> .import dataset/cleaned/cleaned_ecommerce_dataset.csv ecommerce_orders
*/
