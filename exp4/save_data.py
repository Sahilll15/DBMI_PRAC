import pandas as pd
from pymongo import MongoClient

# Step 1: Read Parquet Data
df = pd.read_parquet('data.parquet')

# Step 2: Connect to MongoDB
# Replace 'mongodb://username:password@host:port/database_name' with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')
db = client['database_name']
collection = db['parquest data']  # Replace 'collection_name' with the name of your MongoDB collection

# Step 3: Insert Data into MongoDB
data_dict = df.to_dict(orient='records')
collection.insert_many(data_dict)

print("Data inserted successfully into MongoDB.")
