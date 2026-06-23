import pandas as pd
import os

os.makedirs("data/cleaned", exist_ok=True)
os.makedirs("data/aggregated", exist_ok=True)

print("Loading processed data...")
df = pd.read_parquet("data/processed/patients.parquet")

# Clean data
print("Cleaning data...")
df['admission_date'] = pd.to_datetime(df['admission_date'])
df['age_group'] = pd.cut(df['age'], 
    bins=[0, 30, 50, 70, 100], 
    labels=['18-30', '31-50', '51-70', '70+'])

# Remove outliers
df = df[df['total_charge'] > 0]
df = df[df['los_days'] > 0]

print(f"Clean records: {len(df)}")

# Aggregate by state
state_agg = df.groupby('state').agg(
    total_patients=('patient_id', 'count'),
    avg_charge=('total_charge', 'mean'),
    avg_los=('los_days', 'mean')
).round(2).reset_index()

# Aggregate by specialty
specialty_agg = df.groupby('specialty').agg(
    total_patients=('patient_id', 'count'),
    avg_charge=('total_charge', 'mean'),
    avg_los=('los_days', 'mean')
).round(2).reset_index()

# Save outputs
df.to_parquet("data/cleaned/patients_clean.parquet", index=False)
state_agg.to_csv("data/aggregated/by_state.csv", index=False)
specialty_agg.to_csv("data/aggregated/by_specialty.csv", index=False)

print("\nBy State:")
print(state_agg)
print("\nBy Specialty:")
print(specialty_agg)
print("\nDone!")
