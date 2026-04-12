import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

print("\n--- PASSWORD HISTORY TABLE ---")

cursor.execute("PRAGMA table_info(password_history)")
print(cursor.fetchall())

cursor.execute("SELECT * FROM password_history")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()