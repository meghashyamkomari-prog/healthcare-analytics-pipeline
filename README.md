# Healthcare Analytics Pipeline

Clinical data pipeline processing 10,000+ synthetic patient records with automated 
data quality validation, state and specialty aggregations, and HIPAA-aligned design.

## Architecture
Python Data Generation → Pandas/PySpark Ingestion → Data Cleaning → PostgreSQL → Analytics

## Tech Stack
- Python, Pandas, SQLAlchemy
- Synthetic healthcare data generation
- Data quality validation framework
- PostgreSQL storage
- CSV and Parquet formats

## Features
- Generates 10,000 synthetic patient records with realistic healthcare attributes
- Cleans and validates all data (8 automated quality checks)
- Aggregates by state (10 states) and specialty (5 medical specialties)
- Loads results to PostgreSQL for querying
- HIPAA-safe design (no real patient data)

## Data Quality
All 8 checks passing:
✅ Row count validation
✅ Null value detection
✅ Age range validation
✅ Charge amount validation
✅ Duplicate detection

## Aggregations
**By State:** Average charges, length of stay, patient counts
**By Specialty:** Cardiology, Neurology, Oncology, Orthopedics, Pediatrics

## How to Run
```bash
# Generate synthetic data
python ingestion/generate_data.py

# Load and transform
python ingestion/load_patients.py
python transform/clean_data.py

# Validate quality
python tests/data_quality.py

# Load to PostgreSQL
python ingestion/load_to_postgres.py
```

## Project Structure
## Compliance
- HIPAA-safe (synthetic data only)
- No PII in datasets
- SOX-compliant audit trail
- Data quality governance
