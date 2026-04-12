import hashlib
from database import connect

# Save password hash into history table
def save_password(username, password):

    conn = connect()
    cursor = conn.cursor()

    # Hash password using SHA-256 for secure storage
    hashed = hashlib.sha256(password.encode()).hexdigest()

    # Insert username and hashed password into database
    cursor.execute(
        "INSERT INTO password_history (username, password_hash) VALUES (?, ?)",
        (username, hashed)
    )

    conn.commit()


# Check if password has been previously used by the same user
def check_password_reuse(username, password):

    conn = connect()
    cursor = conn.cursor()

    # Hash input password for comparison
    hashed = hashlib.sha256(password.encode()).hexdigest()

    # Query database for matching username and password hash
    cursor.execute(
        "SELECT * FROM password_history WHERE username=? AND password_hash=?",
        (username, hashed)
    )

    result = cursor.fetchone()

    # Return True if password exists (reused), otherwise False
    return result is not None