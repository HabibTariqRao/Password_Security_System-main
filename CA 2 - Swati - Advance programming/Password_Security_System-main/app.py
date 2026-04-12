from flask import Flask, render_template, request, redirect, session
from functools import wraps

# Import database and system modules
from database import create_tables
from auth import register_user, login_user
from history import save_password, check_password_reuse
from logger import log_activity, get_logs

# Import password analysis modules
from password_checker import check_password_strength
from breach_checker import check_password_breach
from entropy_calculator import calculate_entropy
from pattern_checker import detect_pattern
from password_generator import generate_password

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "secret123"  # Secret key for session management

# Create database tables if not already present
create_tables()


# Login required decorator to protect routes
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Redirect user to login page if not authenticated
        if "user" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return wrapper


# Main route (Password checking dashboard)
@app.route("/", methods=["GET", "POST"])
@login_required
def index():

    # Initialize variables for template rendering
    result = None
    generated = None
    reuse_warning = None

    if request.method == "POST":

        # Handle password generation request
        if "generate" in request.form:
            generated = generate_password()

        else:
            # Get user input and session username
            password = request.form["password"]
            username = session["user"]

            # Perform password analysis
            strength, feedback = check_password_strength(password)
            breached, count = check_password_breach(password)
            entropy = calculate_entropy(password)
            patterns = detect_pattern(password)

            # Check if password has been used before
            is_reused = check_password_reuse(username, password)

            if is_reused:
                reuse_warning = "⚠ Password already used!"
            else:
                # Save password only if not reused
                save_password(username, password)

            # Log user activity
            log_activity(username, strength, breached)

            # Prepare results dictionary for frontend
            result = {
                "strength": strength,
                "feedback": feedback,
                "breached": breached,
                "count": count,
                "entropy": entropy,
                "patterns": patterns
            }

    # Render main dashboard
    return render_template(
        "index.html",
        result=result,
        generated=generated,
        reuse_warning=reuse_warning
    )


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Validate user credentials
        if login_user(username, password):
            session["user"] = username  # Store session
            return redirect("/")

    return render_template("login.html")


# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # Register new user
        register_user(username, password)
        return redirect("/login")

    return render_template("register.html")


# Logs route (Protected)
@app.route("/logs")
@login_required
def logs():

    # Retrieve system logs
    data = get_logs()
    return render_template("logs.html", logs=data)


# Logout route
@app.route("/logout")
@login_required
def logout():
    # Clear session data
    session.clear()
    return redirect("/login")


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)