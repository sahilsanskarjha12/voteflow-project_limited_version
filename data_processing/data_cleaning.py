import pandas as pd

# Read election data
election_data = pd.read_csv("election_data.csv")

# Data cleaning
cleaned_data = election_data.dropna()

# Save cleaned data to new CSV file
cleaned_data.to_csv("cleaned_election_data.csv", index=False)
