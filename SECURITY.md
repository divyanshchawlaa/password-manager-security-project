# Security Documentation

## Authentication Process

The application uses Flask-Login for user authentication and session management.

### Registration

1. User enters username, email, and password.
2. Password strength validation is performed.
3. Password is hashed using bcrypt.
4. User information is stored in SQLite.

### Login

1. User enters email and password.
2. Stored bcrypt hash is retrieved.
3. Password is verified using bcrypt.
4. Secure session is created.

---

## Password Storage

User account passwords are never stored in plain text.

The application uses:

* bcrypt hashing
* Salted password hashes
* One-way password verification

Example:

```text
Password123!
```

becomes a bcrypt hash before storage.

---

## Credential Storage

Website credentials are encrypted before being stored.

Encryption method:

* Fernet symmetric encryption
* Cryptography library

Process:

1. User enters website password.
2. Password is encrypted.
3. Encrypted value is stored in SQLite.
4. Password is decrypted only when displayed to the authenticated user.

---

## Database Security

The application uses SQLite with SQLAlchemy ORM.

Security benefits:

* Parameterized queries
* Reduced SQL injection risk
* Structured database access

---

## Session Security

Flask-Login is used to:

* Protect authenticated routes
* Maintain user sessions
* Restrict access to user-owned credentials

Unauthenticated users cannot access protected pages.

---

## Password Strength Enforcement

User passwords must contain:

* At least 8 characters
* Uppercase letter
* Lowercase letter
* Number
* Special character

Weak passwords are rejected during registration.

---

## Security Controls Implemented

| Threat              | Protection                    |
| ------------------- | ----------------------------- |
| Weak Passwords      | Password Strength Validation  |
| Password Theft      | bcrypt Hashing                |
| Database Exposure   | Fernet Encryption             |
| SQL Injection       | SQLAlchemy ORM                |
| Unauthorized Access | Flask-Login Authentication    |
| Duplicate Accounts  | Username and Email Validation |

---

## Future Security Improvements

The following features could further improve security:

* Multi-Factor Authentication (MFA)
* HTTPS Deployment
* Password Breach Detection
* Account Lockout After Failed Logins
* Secure Password Reset Workflow

---

## Conclusion

This project demonstrates the implementation of fundamental cybersecurity principles including authentication, authorization, password hashing, encryption, secure session management, and input validation within a password manager application.
