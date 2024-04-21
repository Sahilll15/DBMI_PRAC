


import mysql.connector
import pandas as pd


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dmbi"
)


cursor = conn.cursor()


data = [
    ("John", 30, "New York"),
    ("Alice", 25, "Los Angeles"),
    ("Bob", 35, "Chicago")
]

df_from_parquet = pd.read_parquet('data.parquet')


# Insert data into MySQL table
for index, row in df_from_parquet.iterrows():
    sql = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
    cursor.execute(sql, tuple(row))




# cursor.executemany(sql, data)


conn.commit()


cursor.close()
conn.close()

print("Data inserted successfully into MySQL database.")
