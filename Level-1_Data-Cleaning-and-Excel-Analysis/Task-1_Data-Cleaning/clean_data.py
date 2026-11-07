"""
Task 1: Data Understanding & Cleaning
Primeor Solutions - E-Commerce Data Analytics Internship
Level 1: Task 1

This script performs end-to-end data understanding, cleaning, and preprocessing:
1. Load raw dataset and inspect schema & statistical properties
2. Detect and remove duplicate records
3. Strip leading/trailing whitespaces and standardize text columns
4. Convert and sanitize numeric fields (e.g. Sales with commas)
5. Handle missing / null values (Customer Name & Profit)
6. Standardize date formats to ISO YYYY-MM-DD
7. Export cleaned dataset to CSV and Excel
"""

import os
import pandas as pd
import numpy as np

def clean_ecommerce_data(raw_csv_path: str, output_csv_path: str):
    print("=" * 60)
    print("STEP 1: Loading raw dataset...")
    df = pd.read_csv(raw_csv_path)
    total_raw_rows = len(df)
    print(f"Total raw records: {total_raw_rows}")
    print(f"Columns ({len(df.columns)}): {list(df.columns)}")

    # 1. Duplicates
    print("\nSTEP 2: Checking and removing duplicates...")
    dups_count = df.duplicated().sum()
    print(f"Duplicate records found: {dups_count}")
    df = df.drop_duplicates()
    print(f"Records remaining after deduplication: {len(df)}")

    # 2. Whitespace and text standardization
    print("\nSTEP 3: Standardizing text formatting...")
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace('nan', np.nan)

    # 3. Numeric conversion for sales
    print("\nSTEP 4: Fixing numeric fields (sales formatting)...")
    df['sales'] = df['sales'].astype(str).str.replace(',', '').str.replace('$', '').str.strip()
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

    # 4. Handle missing values
    print("\nSTEP 5: Handling missing / null values...")
    missing_cust = df['customer_name'].isna().sum()
    missing_profit = df['profit'].isna().sum()
    print(f"Missing Customer Names: {missing_cust}")
    print(f"Missing Profit values: {missing_profit}")

    # Impute customer name
    df['customer_name'] = df['customer_name'].fillna('Unknown Customer')

    # Impute profit using median per sub-category
    subcat_median_profit = df.groupby('sub_category')['profit'].transform('median')
    df['profit'] = df['profit'].fillna(subcat_median_profit).round(2)

    # 5. Fix dates
    print("\nSTEP 6: Standardizing date formats to YYYY-MM-DD...")
    df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True).dt.strftime('%Y-%m-%d')
    df['ship_date'] = pd.to_datetime(df['ship_date'], format='mixed', dayfirst=True).dt.strftime('%Y-%m-%d')

    # Verify 0 nulls remaining
    remaining_nulls = df.isnull().sum().sum()
    print(f"\nTotal null values after cleaning: {remaining_nulls}")

    # Save cleaned CSV
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
    df.to_csv(output_csv_path, index=False)
    print(f"\nCleaned dataset successfully saved to: {output_csv_path}")
    print("=" * 60)
    return df

if __name__ == "__main__":
    raw_path = os.path.join("dataset", "raw", "Dataset.csv")
    cleaned_path = os.path.join("dataset", "cleaned", "cleaned_ecommerce_dataset.csv")
    clean_ecommerce_data(raw_path, cleaned_path)
