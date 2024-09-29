import pandas as pd

# Read a CSV file (make sure to adjust the file path)
df = pd.read_csv('data.csv')

# Display the contents of the CSV file
print(df)

# Use the 'describe' function to get statistics
print(df.describe())
