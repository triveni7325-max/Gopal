import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS published_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER
)
""")

conn.commit()
conn.close()

print("Table created successfully")