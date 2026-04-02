import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("ALTER TABLE quizzes ADD COLUMN time INTEGER")

conn.commit()
conn.close()

print("Column added")