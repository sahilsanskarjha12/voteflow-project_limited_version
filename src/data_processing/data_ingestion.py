# data_ingestion.py
import pandas as pd

def ingest_data(file_path):
    """Ingest raw election data from CSV file."""
    data = pd.read_csv(file_path)
    return data

# Example usage
file_path = "data/raw/election_data.csv"
election_data = ingest_data(file_path)
print(election_data.head())
