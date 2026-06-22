from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    ValidationError
)

import re


def strong_password(form, field):

    password = field.data

    if len(password) < 8:
        raise ValidationError(
            "Password must be at least 8 characters."
        )

    if not re.search(r"[A-Z]", password):
        raise ValidationError(
            "Password must contain an uppercase letter."
        )

    if not re.search(r"[a-z]", password):
        raise ValidationError(
            "Password must contain a lowercase letter."
        )

    if not re.search(r"\d", password):
        raise ValidationError(
            "Password must contain a number."
        )

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError(
            "Password must contain a special character."
        )


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            strong_password
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


class CredentialForm(FlaskForm):

    website = StringField(
        "Website",
        validators=[DataRequired()]
    )

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save")