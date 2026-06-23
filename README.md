# 🔐 Secure Password Manager

A secure web-based password manager developed using Python, Flask, SQLite, and modern cybersecurity principles.

This project demonstrates secure authentication, encrypted credential storage, password generation, and password management through a user-friendly web interface.

---

## 🚀 Features

### 👤 User Authentication

* User Registration
* User Login & Logout
* Session Management
* Password Hashing with bcrypt

### 🔒 Credential Management

* Add Credentials
* View Stored Credentials
* Edit Credentials
* Delete Credentials
* Search Credentials

### 🛡️ Security Features

* Password Encryption using Fernet (AES-based encryption)
* Password Hashing using bcrypt
* Password Strength Validation
* Duplicate Username Prevention
* Duplicate Email Prevention
* SQLAlchemy ORM Protection against SQL Injection
* Secure Session Handling with Flask-Login

### 🔑 Password Generator

Generate strong random passwords using Python's secure `secrets` module.

Example:

```text
M@9xQ#2vLp!7RwK8
```

---

## 🏗️ Technologies Used

| Technology            | Purpose             |
| --------------------- | ------------------- |
| Python                | Backend Development |
| Flask                 | Web Framework       |
| SQLite                | Database            |
| SQLAlchemy            | ORM                 |
| Flask-Login           | Authentication      |
| Flask-Bcrypt          | Password Hashing    |
| Cryptography (Fernet) | Password Encryption |
| Bootstrap 5           | User Interface      |

---

## 📂 Project Structure

```text
password-manager/
│
├── app.py
├── config.py
├── models.py
├── forms.py
├── encryption.py
├── password_generator.py
├── generate_key.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_credential.html
│   ├── edit_credential.html
│   ├── view_credentials.html
│   └── generate_password.html
│
├── requirements.txt
├── README.md
└── setup.sh
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/divyanshchawlaa/password-manager-security-project.git
cd password-manager-security-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Encryption Key

```bash
python generate_key.py
```

### Run Application

```bash
python app.py
```

---

## 🌐 Application URL

```text
http://127.0.0.1:5000
```

---

## 🔐 Security Implementation

### Password Hashing

User account passwords are hashed using bcrypt before being stored in the database.

### Password Encryption

Stored credentials are encrypted using Fernet symmetric encryption before being written to the database.

### Authentication & Sessions

Flask-Login manages authenticated user sessions and protects restricted routes.

### Password Strength Enforcement

User passwords must contain:

* Minimum 8 characters
* Uppercase letter
* Lowercase letter
* Number
* Special character

### Database Security

SQLAlchemy ORM is used to avoid direct SQL queries and reduce SQL injection risks.

---

## 🧪 Testing

The application was tested for:

* User Registration
* Login Authentication
* Session Management
* Password Encryption & Decryption
* Credential CRUD Operations
* Password Generation
* Search Functionality
* Input Validation

---

## 🔮 Future Improvements

* Multi-Factor Authentication (MFA)
* Password Breach Detection
* Password Sharing
* Secure Cloud Synchronization
* Browser Extension Support

---

## 👨‍💻 Author

**Divyansh Chawla**

Cybersecurity Project — Secure Password Manager

June 2026
