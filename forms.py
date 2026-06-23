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

    errors = []

    if len(password) < 8:
        errors.append(
            "at least 8 characters"
        )

    if not re.search(r"[A-Z]", password):
        errors.append(
            "an uppercase letter"
        )

    if not re.search(r"[a-z]", password):
        errors.append(
            "a lowercase letter"
        )

    if not re.search(r"\d", password):
        errors.append(
            "a number"
        )

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append(
            "a special character"
        )

    if errors:

        raise ValidationError(
            "Password must contain: " +
            ", ".join(errors)
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

    def validate_username(self, username):

        from models import User

        user = User.query.filter_by(
            username=username.data
        ).first()

        if user:
            raise ValidationError(
                "Username already exists."
            )

    def validate_email(self, email):

        from models import User

        user = User.query.filter_by(
            email=email.data
        ).first()

        if user:
            raise ValidationError(
                "Email already registered."
            )

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