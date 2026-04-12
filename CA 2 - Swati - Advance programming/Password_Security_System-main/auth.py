import bcrypt
from database import connect

# Register new user
def register_user(username, password):

    conn = connect()
    cursor = conn.cursor()

    # Hash password using bcrypt
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        # Insert new user into database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hashed))
        conn.commit()
        return True
    except:
        return False


# Login user authentication
def login_user(username, password):

    conn = connect()
    cursor = conn.cursor()

    # Retrieve stored password hash
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[0]

        # Compare hashed password
        if bcrypt.checkpw(password.encode(), stored_password):
            return True

    return False