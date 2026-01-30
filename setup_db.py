import sqlite3

#method to initialise table if it does not exist at runtime
def create_database():
    connection = sqlite3.connect("news.db")
    cursor = connection.cursor()


    sql_command = """
    CREATE TABLE IF NOT EXISTS stories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline VARCHAR(150) NOT NULL, 
    link VARCHAR(150) NOT NULL UNIQUE,
    rank INTEGER,
    scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(sql_command)
    connection.commit()
    connection.close()


create_database()


# test method to see if table was configured correctly
# def add_values():
#     connection = sqlite3.connect("news.db")
#     cursor = connection.cursor()

#     cursor.execute("""INSERT INTO stories (headline,link,rank) VALUES(?,?,?) """,["test","test.co.uk",1])
#     connection.commit()
#     connection.close()

# add_values()