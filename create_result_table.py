import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    quiz_id INTEGER,
    score INTEGER,
    right_ans INTEGER,
    wrong_ans INTEGER,
    skipped INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()