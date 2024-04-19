import pandas as pd

# Read transformed election data
transformed_data = pd.read_csv("transformed_election_data.csv")

# Data aggregation
aggregated_data = transformed_data.mean()

# Print aggregated data
print(aggregated_data)
