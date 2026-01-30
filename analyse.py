import sqlite3
import pandas as pd

connection = sqlite3.connect("news.db")
df = pd.read_sql_query("SELECT * FROM stories",connection)
connection.close()

print("dataframe shape, rows, columns")
print(df.shape)

print("first few rows")
print(df.head())