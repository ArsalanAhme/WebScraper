import sqlite3
import pandas as pd

connection = sqlite3.connect("news.db")
df = pd.read_sql_query("SELECT * FROM stories",connection)
connection.close()

df["domain"] = df['link'].str.extract(r'://(.*?)/', expand=False)

source_count = df['domain'].value_counts()

print(source_count.head(5))

# print("dataframe shape, rows, columns")
# print(df.shape)

# print("first few rows")
# print(df.head())


print("\ntop words within headlines")
stop_words = ['the', 'a', 'to', 'of', 'in', 'and', 'is', 'for', 'on', 'with', 'by', 'at', 'from', 'it']


all_words= df['headline'].str.lower().str.split().explode()
interesting_words = all_words[~all_words.isin(stop_words)]


print(interesting_words.value_counts().head(5))