import pandas as pd

# Create a date range
dates = pd.date_range('2023-01-01', periods=10)

# Create a series with the dates as indices
series = pd.Series(range(10), index=dates)

# Display the series
print(series)

# Display specific values by index
print("Value on specific date:", series['2023-01-05'])
