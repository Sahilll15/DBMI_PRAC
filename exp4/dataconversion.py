import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Parquet file
df.to_parquet('data.parquet', index=False)
