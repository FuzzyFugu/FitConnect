"""Authentication routes: registration, login and logout.

Owned by the Login/Frontend developer. Handles account creation with hashed
passwords and session management via Flask-Login.
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from app.extensions import db
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Guard against duplicate accounts before writing to the DB.
        if User.query.filter_by(email=form.email.data).first():
            flash("An account with that email already exists.", "danger")
            return render_template("auth/register.html", form=form)
        if User.query.filter_by(username=form.username.data).first():
            flash("That username is taken.", "danger")
            return render_template("auth/register.html", form=form)

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created — welcome to FitConnect!", "success")
        login_user(user)
        return redirect(url_for("main.dashboard"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            # Respect the page the user was originally trying to reach.
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.dashboard"))
        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))
