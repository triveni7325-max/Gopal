import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# column add
cur.execute("ALTER TABLE questions ADD COLUMN marks INTEGER")

# old data update
cur.execute("UPDATE questions SET marks = 1")

conn.commit()
conn.close()

print("Marks column added")