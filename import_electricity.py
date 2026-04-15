import pandas as pd
from db_connection import get_connection

# Load CSV file
df = pd.read_csv("data/european_wholesale_electricity_price_data_daily.csv")

# Keep only needed columns
df = df[["Country", "ISO3 Code", "Date", "Price (EUR/MWhe)"]]

# Convert rows into list of tuples
data = list(df.itertuples(index=False, name=None))

# Connect to database
conn = get_connection()
cursor = conn.cursor()

sql = """
INSERT INTO electricity_prices (country, iso3_code, date, price)
VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
price = VALUES(price)
"""

# Insert all rows at once (FAST)
cursor.executemany(sql, data)

conn.commit()

print(f"{cursor.rowcount} rows imported successfully!")

cursor.close()
conn.close()
