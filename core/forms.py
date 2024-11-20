from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import TextInput, PasswordInput, EmailInput, SubmitInput


class RegistrationForm(FlaskForm):
    user = StringField(
        "Username",
        widget=TextInput(),
        validators=[DataRequired(), Length(min=4, max=25)],
    )
    email = StringField(
        "Email", widget=EmailInput(), validators=[Length(min=6, max=35), Email()]
    )
    Password = PasswordField(
        "New Password",
        widget=PasswordInput(),
        validators=[
            DataRequired(),
            EqualTo("confirm", message="Password must match"),
        ],
    )
    confirm = PasswordField(
        "repeat password",
        widget=PasswordInput(),
    )
    Submit = SubmitField("Register", widget=SubmitInput())


class loginForm(FlaskForm):
    email = StringField(
        "Email", widget=EmailInput(), validators=[Length(min=6, max=35), Email()]
    )

    Password = PasswordField(
        "Password",
        widget=PasswordInput(),
    )
    rember = BooleanField("Remember me")
    Submit = SubmitField("Login", widget=SubmitInput())
