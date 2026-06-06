import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

# Show first 10 rows
print("Sample data:")
print(df.head())

# Simple aggregation
summary = df.groupby("region")["sales"].sum()
print("\nSales by region:")
print(summary)