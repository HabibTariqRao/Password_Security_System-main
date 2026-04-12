import sqlite3

# Establish database connection
def connect():
    return sqlite3.connect("database.db")


# Create required tables
def create_tables():

    conn = connect()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Password history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS password_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password_hash TEXT
    )
    """)

    # Logs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        strength TEXT,
        breached INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()