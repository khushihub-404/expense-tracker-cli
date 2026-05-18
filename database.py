import sqlite3

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    type TEXT,
    amount REAL
)
""")

conn.commit()
conn.close()

print("Database Created!")