import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("Loading patient data...")

# Read raw data
df = pd.read_csv("data/raw/patients.csv")

print(f"Total records: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Basic validation
print("\nNull counts:")
print(df.isnull().sum())

# Data type validation
print("\nData types:")
print(df.dtypes)

# Save as parquet
df.to_parquet("data/processed/patients.parquet", index=False)
print("\nSaved to data/processed/patients.parquet")
print("Done!")
