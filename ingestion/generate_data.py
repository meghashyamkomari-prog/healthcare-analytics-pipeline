import pandas as pd
import random
import os
from datetime import datetime, timedelta

random.seed(42)
base_path = "/mnt/c/Users/megha/healthcare-analytics-pipeline"
os.makedirs(f"{base_path}/data/raw", exist_ok=True)

# Generate synthetic patient data
states = ['TX', 'CA', 'NY', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
specialties = ['Cardiology', 'Orthopedics', 'Neurology', 'Oncology', 'Pediatrics']
conditions = ['Diabetes', 'Hypertension', 'Asthma', 'Heart Disease', 'Cancer']

patients = []
for i in range(10000):
    admit_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    patients.append({
        'patient_id': f'P{i+1:06d}',
        'age': random.randint(18, 90),
        'gender': random.choice(['M', 'F']),
        'state': random.choice(states),
        'specialty': random.choice(specialties),
        'condition': random.choice(conditions),
        'admission_date': admit_date.strftime('%Y-%m-%d'),
        'los_days': random.randint(1, 30),
        'total_charge': round(random.uniform(1000, 50000), 2),
        'insurance_type': random.choice(['Medicare', 'Medicaid', 'Private', 'Uninsured'])
    })

df = pd.DataFrame(patients)
df.to_csv(f'{base_path}/data/raw/patients.csv', index=False)
print(f"Generated {len(df)} patient records")
print("Done!")
