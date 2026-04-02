import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("INSERT INTO categories (name) VALUES ('GK')")
cur.execute("INSERT INTO categories (name) VALUES ('Railway')")

cur.execute("INSERT INTO quizzes (category_id,quiz_name) VALUES (1,'GK Quiz 1')")
cur.execute("INSERT INTO quizzes (category_id,quiz_name) VALUES (1,'GK Quiz 2')")
cur.execute("INSERT INTO quizzes (category_id,quiz_name) VALUES (2,'Railway Quiz 1')")

conn.commit()
conn.close()

print("Data inserted")