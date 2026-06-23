import pandas as pd

print("Running data quality checks...")
print("=" * 50)

df = pd.read_parquet("data/cleaned/patients_clean.parquet")

checks = []

# Check 1: Row count
count = len(df)
checks.append(("Row count > 1000", count > 1000, count))

# Check 2: No nulls in critical columns
for col in ['patient_id', 'age', 'state', 'condition']:
    null_count = df[col].isnull().sum()
    checks.append((f"No nulls in {col}", null_count == 0, null_count))

# Check 3: Age range valid
age_valid = df['age'].between(0, 120).all()
checks.append(("Age between 0-120", age_valid, df['age'].max()))

# Check 4: Charges positive
charges_valid = (df['total_charge'] > 0).all()
checks.append(("All charges > 0", charges_valid, df['total_charge'].min()))

# Check 5: No duplicate patient IDs
duplicates = df['patient_id'].duplicated().sum()
checks.append(("No duplicate patient IDs", duplicates == 0, duplicates))

# Print results
passed = 0
failed = 0
for check_name, passed_check, value in checks:
    status = "PASS ✅" if passed_check else "FAIL ❌"
    print(f"{status} | {check_name} | value={value}")
    if passed_check:
        passed += 1
    else:
        failed += 1

print("=" * 50)
print(f"Results: {passed} passed, {failed} failed")
print("Done!")
