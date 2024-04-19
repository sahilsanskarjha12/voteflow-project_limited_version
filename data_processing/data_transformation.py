import pandas as pd

# Read cleaned election data
cleaned_data = pd.read_csv("cleaned_election_data.csv")

# Data transformation
transformed_data = cleaned_data.groupby('region').sum()

# Save transformed data to new CSV file
transformed_data.to_csv("transformed_election_data.csv")
