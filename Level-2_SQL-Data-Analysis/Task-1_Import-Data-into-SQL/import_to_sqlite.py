import sqlite3
import pandas as pd
import os

def build_database():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dataset/cleaned/cleaned_ecommerce_dataset.csv'))
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ecommerce_analysis.db'))
    
    print(f"Loading data from: {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Ensure correct data types
    df['order_date'] = pd.to_datetime(df['order_date']).dt.strftime('%Y-%m-%d')
    df['ship_date'] = pd.to_datetime(df['ship_date']).dt.strftime('%Y-%m-%d')
    
    print(f"Connecting to SQLite database: {db_path}")
    conn = sqlite3.connect(db_path)
    
    # Write to table
    df.to_sql('ecommerce_orders', conn, if_exists='replace', index=False)
    
    # Create indexes for performance
    cursor = conn.cursor()
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_order_date ON ecommerce_orders(order_date);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_customer_name ON ecommerce_orders(customer_name);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_category_sub ON ecommerce_orders(category, sub_category);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_region_market ON ecommerce_orders(region, market);")
    conn.commit()
    
    # Verify count
    count = cursor.execute("SELECT COUNT(*) FROM ecommerce_orders;").fetchone()[0]
    print(f"Successfully imported {count} rows into 'ecommerce_orders'.")
    conn.close()

if __name__ == '__main__':
    build_database()
