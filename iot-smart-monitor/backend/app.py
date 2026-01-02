import os
from flask import Flask, render_template, redirect, url_for
from models import db, MotionEvent

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Config (ready for AWS later)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.getenv("DATABASE_URL") or
    "sqlite:///" + os.path.join(BASE_DIR, "motion.db")
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# -----------------------
# ROUTES
# -----------------------

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

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
# RUN
# -----------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
