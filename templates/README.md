# Secure Password Manager

## Project Overview

This project is a secure password manager developed using Python, Flask, SQLite, and modern cybersecurity practices.

The application allows users to:

* Register and authenticate securely
* Store website credentials
* Encrypt stored passwords
* Generate strong passwords
* Search stored credentials
* Manage credentials through a web interface

---

## Features

### User Authentication

* User registration
* User login and logout
* Password hashing using bcrypt
* Session management using Flask-Login

### Credential Management

* Add credentials
* View credentials
* Edit credentials
* Delete credentials
* Search credentials

### Security Features

* Password encryption using Fernet encryption
* Password hashing using bcrypt
* Strong password validation
* Duplicate username prevention
* Duplicate email prevention
* SQLAlchemy ORM to reduce SQL injection risks

### Password Generator

* Secure random password generation
* Uses Python secrets module

---

## Technologies Used

* Python
* Flask
* Flask-WTF
* Flask-Login
* Flask-Bcrypt
* SQLAlchemy
* SQLite
* Cryptography (Fernet)
* Bootstrap 5

---

## Installation

### Clone Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd password-manager

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Generate Encryption Key

python generate_key.py

### Run Application

python app.py

---

## Default Application URL

http://127.0.0.1:5000

---

## Security Measures

### Password Hashing

User passwords are hashed using bcrypt before storage.

### Password Encryption

Stored credentials are encrypted using Fernet symmetric encryption.

### Authentication

Flask-Login is used to manage authenticated sessions.

### Password Strength Validation

Passwords must contain:

* Minimum 8 characters
* Uppercase letter
* Lowercase letter
* Number
* Special character

### Database Security

SQLAlchemy ORM is used instead of raw SQL queries to reduce SQL injection risks.

---

## Future Improvements

* Multi-Factor Authentication (MFA)
* Password sharing
* Browser extension support
* Password breach detection
* Secure cloud synchronization

---

## Author

Divyansh Chawla

Cybersecurity Project – Secure Password Manager
