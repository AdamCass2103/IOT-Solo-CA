from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motion.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@app.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run()
