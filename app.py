from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash
)

from config import Config

from models import db, User, Credential

from forms import (
    RegisterForm,
    LoginForm,
    CredentialForm
)

from encryption import (
    encrypt_password,
    decrypt_password
)

from password_generator import generate_password

from flask_bcrypt import Bcrypt

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "register.html",
        form=form
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password_hash,
            form.password.data
        ):

            login_user(user)

            flash(
                f"Welcome back, {user.username}!",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid email or password.",
            "danger"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "login.html",
        form=form
    )


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html",
        username=current_user.username
    )


@app.route("/add", methods=["GET", "POST"])
@login_required
def add_credential():

    form = CredentialForm()

    if form.validate_on_submit():

        encrypted_password = encrypt_password(
            form.password.data
        )

        credential = Credential(
            website=form.website.data,
            username=form.username.data,
            encrypted_password=encrypted_password,
            user_id=current_user.id
        )

        db.session.add(credential)
        db.session.commit()

        flash(
            "Credential saved successfully.",
            "success"
        )

        return redirect(
            url_for("view_credentials")
        )

    return render_template(
        "add_credential.html",
        form=form
    )


@app.route("/view")
@login_required
def view_credentials():

    credentials = Credential.query.filter_by(
        user_id=current_user.id
    ).all()

    credential_list = []

    for credential in credentials:

        credential_list.append({
            "id": credential.id,
            "website": credential.website,
            "username": credential.username,
            "password": decrypt_password(
                credential.encrypted_password
            )
        })

    return render_template(
        "view_credentials.html",
        credentials=credential_list
    )


@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_credential(id):

    credential = Credential.query.get_or_404(id)

    if credential.user_id != current_user.id:
        return "Unauthorized"

    form = CredentialForm()

    if form.validate_on_submit():

        credential.website = form.website.data
        credential.username = form.username.data

        credential.encrypted_password = encrypt_password(
            form.password.data
        )

        db.session.commit()

        flash(
            "Credential updated successfully.",
            "success"
        )

        return redirect(
            url_for("view_credentials")
        )

    form.website.data = credential.website
    form.username.data = credential.username
    form.password.data = decrypt_password(
        credential.encrypted_password
    )

    return render_template(
        "edit_credential.html",
        form=form
    )


@app.route("/delete/<int:id>")
@login_required
def delete_credential(id):

    credential = Credential.query.get_or_404(id)

    if credential.user_id != current_user.id:
        return "Unauthorized"

    db.session.delete(credential)
    db.session.commit()

    flash(
        "Credential deleted successfully.",
        "warning"
    )

    return redirect(
        url_for("view_credentials")
    )


@app.route("/generate", methods=["GET", "POST"])
@login_required
def generate_password_page():

    generated_password = None

    if request.method == "POST":

        generated_password = generate_password()

    return render_template(
        "generate_password.html",
        password=generated_password
    )


@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "You have been logged out.",
        "info"
    )

    return redirect(
        url_for("login")
    )


if __name__ == "__main__":
    app.run(debug=True)