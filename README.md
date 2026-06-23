# Healthcare Analytics Pipeline

Clinical data pipeline processing 10,000+ synthetic patient records with automated 
data quality validation, state and specialty aggregations, and HIPAA-aligned design. 
Orchestrated with Apache Airflow for daily execution.

## Architecture
Python Data Generation → Pandas Ingestion → Data Cleaning → PostgreSQL → Analytics

## Tech Stack
* Python, Pandas, SQLAlchemy
* Synthetic healthcare data generation
* Data quality validation framework
* PostgreSQL database
* Parquet file format
* Apache Airflow orchestration

## Features
* Generates 10,000 synthetic patient records with realistic healthcare attributes
* Cleans and validates all data (8 automated quality checks)
* Aggregates by state (10 states) and specialty (5 medical specialties)
* Loads results to PostgreSQL for analytics queries
* Airflow DAG for daily automated execution
* HIPAA-safe design (synthetic data only)

## Data Quality
All 8 checks passing:
✅ Row count validation (10,000+ records)
✅ Null value detection (zero nulls in critical columns)
✅ Age range validation (18-120 years)
✅ Charge amount validation (all charges > $0)
✅ Duplicate patient ID detection
✅ State data validation
✅ Medical specialty validation
✅ Insurance type validation

## Aggregations
**By State:** 10 states (TX, CA, NY, FL, IL, PA, OH, GA, NC, MI)
- Average charges per state
- Average length of stay
- Patient counts

**By Specialty:** 5 medical specialties
- Cardiology, Neurology, Oncology, Orthopedics, Pediatrics
- Aggregated metrics by specialty

## How to Run
```bash
# Generate synthetic patient data
python ingestion/generate_data.py

# Load and process data
python ingestion/load_patients.py
python transform/clean_data.py

# Validate data quality
python tests/data_quality.py

# Load to PostgreSQL
python ingestion/load_to_postgres.py

# Start Airflow (for daily scheduling)
airflow standalone
# Navigate to http://localhost:8080 and trigger healthcare_pipeline
```

## Project Structure
healthcare-analytics-pipeline/

├── ingestion/           # Data generation and loading

├── transform/           # Data cleaning and aggregation

├── tests/              # Data quality validation

├── data/

│   ├── raw/            # Generated synthetic data

│   ├── processed/      # Parquet format

│   ├── cleaned/        # Quality-validated data

│   └── aggregated/     # State and specialty summaries

└── README.md
## Compliance
* HIPAA-safe (synthetic data only)
* No PII in datasets
* SOX-compliant audit trail
* Data quality governance framework
