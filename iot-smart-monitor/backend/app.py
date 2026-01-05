import os
from flask import Flask, render_template, redirect, url_for
from models import db, MotionEvent

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# -----------------------
# Flask App Setup
# -----------------------
template_dir = os.path.join(BASE_DIR, '..', 'frontend', 'templates')
static_dir = os.path.join(BASE_DIR, '..', 'frontend', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# -----------------------
# Database Config (MySQL)
# -----------------------
MYSQL_USER = os.getenv("MYSQL_USER", "root")           # XAMPP root user
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")       # root password (blank if none)
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")      # localhost
MYSQL_DB = os.getenv("MYSQL_DB", "iot_motion_monitor") # your database

# SQLAlchemy URI for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret-key")

db.init_app(app)

# -----------------------
# ROUTES
# -----------------------
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/dashboard-shortcut")
def dashboard_shortcut():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    events = MotionEvent.query.order_by(MotionEvent.timestamp.desc()).all()
    return render_template("dashboard.html", events=events)

@app.route("/history")
def history():
    events = MotionEvent.query.all()
    return render_template("history.html", events=events)

@app.route("/test-insert")
def test_insert():
    event = MotionEvent(detected=True)
    db.session.add(event)
    db.session.commit()
    return redirect(url_for("dashboard"))

# -----------------------
# RUN APP
# -----------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # creates tables in MySQL if they don't exist
    app.run(debug=True)
