import sqlite3


connection = sqlite3.connect("news.db")
cursor = connection.cursor()



cursor.execute("SELECT COUNT(*) FROM stories")
count = cursor.fetchone()[0]

print(f"total stories in database {count}")

print("\n--- Top 3 Most Recent ---")
cursor.execute("SELECT * FROM stories ORDER BY id DESC LIMIT 3")
for row in cursor.fetchall():
    print(row)

connection.close()