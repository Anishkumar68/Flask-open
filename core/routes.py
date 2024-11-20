from core.forms import RegistrationForm, loginForm
from flask import render_template, redirect, url_for, flash
from core import app


@app.route("/")
@app.route("/home")
def home():
    title = "home"
    user = "anish"
    return render_template("home.html", title="home", user="anish")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created as {form.user.data}!")
        return redirect(url_for("home"))

    return render_template("signup.html", title="Registration", form=form)


@app.route("/login")
def login():
    form = loginForm()
    if form.validate_on_submit():
        flash(f" Welcome {form.user.data}!")
        return redirect(url_for("home"))
    return render_template("login.html", title="login", form=form)
