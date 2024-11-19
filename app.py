from flask import Flask, render_template
import os
from dotenv import load_dotenv
from flask_wtf import CSRFProtect
from forms import RegistrationForm, loginForm


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("secret_key")

csrf = CSRFProtect(app)


@app.route("/")
@app.route("/home")
def home():
    title = "home"
    user = "anish"
    return render_template("home.html", title="home", user="anish")


@app.route("/signup")
def signup():
    form = RegistrationForm()
    return render_template("signup.html", title="Registration", form=form)


@app.route("/login")
def login():
    form = loginForm()
    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
