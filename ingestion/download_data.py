import requests
import os

# CMS Medicare Provider Data - free public dataset
URL = "https://data.cms.gov/provider-data/sites/default/files/resources/b12b765a8a0e6e9b9e5e5d1e9f5e9f5e_1709055695/Physician_Compare_National_Downloadable_File.csv"

# Alternative smaller dataset
URL = "https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/customers/customers-100000.csv"

os.makedirs("data/raw", exist_ok=True)

print("Downloading dataset...")
response = requests.get(URL)
with open("data/raw/healthcare_data.csv", "wb") as f:
    f.write(response.content)
print(f"Downloaded {len(response.content)} bytes")
print("Done!")
