import random
import sqlite3

connection = sqlite3.connect("news.db")
cursor = connection.cursor()

cursor.execute("SELECT headline, link FROM stories ORDER BY random() LIMIT 1")
# need to have it in a variable most likely

story = cursor.fetchone()

connection.close()



if story:
    print(f"you should read {story[0]}")
    print(f"link: {story[1]}")
else:
    print("no stories found in database")



buzz_words = ["SHOCKING:", "UNBELIEVABLE:", "MUST READ:", "GONE WRONG:"]
val = random.randint(0,len(buzz_words))

print(f"{buzz_words[val]} {story[0].upper()} ")
