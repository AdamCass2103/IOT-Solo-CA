import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import db, MotionEvent, User

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

template_dir = os.path.join(BASE_DIR, '..', 'frontend', 'templates')
static_dir = os.path.join(BASE_DIR, '..', 'frontend', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# -----------------------
# MySQL CONFIG
# -----------------------
MYSQL_USER = "flaskuser"
MYSQL_PASSWORD = ""
MYSQL_HOST = "127.0.0.1"
MYSQL_DB = "iot_motion_monitor"

print("Using DB config:", MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://root@localhost/iot_motion_monitor"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "dev-secret-key"

db.init_app(app)

# -----------------------
# ROUTES
# -----------------------

@app.route("/test-insert")
def test_insert():
    event = MotionEvent(detected=True, led_state=True)
    db.session.add(event)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/toggle-led/<int:event_id>")
def toggle_led(event_id):
    event = MotionEvent.query.get(event_id)
    if event:
        event.led_state = not event.led_state
        db.session.commit()
    return redirect(url_for("dashboard"))


@app.route("/history")
def history():
    events = MotionEvent.query.all()
    return render_template("history.html", events=events)

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("signup"))

        if User.query.filter_by(email=email).first():
            flash("Email already exists")
            return redirect(url_for("signup"))

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please log in.")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:  # Require login
        return redirect(url_for("login"))

    events = MotionEvent.query.order_by(MotionEvent.timestamp.desc()).all()
    return render_template("dashboard.html", events=events)



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# -----------------------
# RUN
# -----------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)


