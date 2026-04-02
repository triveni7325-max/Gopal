import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS published_quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER
)
""")

conn.commit()
conn.close()

print("Table created successfully")