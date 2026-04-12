from database import connect

# Store user activity logs
def log_activity(username, strength, breached):

    conn = connect()
    cursor = conn.cursor()

    # Insert log entry with username, password strength, and breach status
    cursor.execute("""
    INSERT INTO logs (username, strength, breached)
    VALUES (?, ?, ?)
    """, (username, strength, int(breached)))

    conn.commit()


# Retrieve logs in descending order of timestamp
def get_logs():

    conn = connect()
    cursor = conn.cursor()

    # Fetch all logs ordered by latest activity first
    cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC")

    return cursor.fetchall()