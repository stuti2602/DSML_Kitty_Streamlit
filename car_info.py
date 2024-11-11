# Create a new file called check_data.py
import pandas as pd

# Load CSV
df = pd.read_csv('cars24-car-price-cleaned.csv')

# Print all column names
print("\nColumn names in your CSV:")
print(df.columns.tolist())

# Show first few rows
print("\nFirst few rows of your data:")
print(df.head())