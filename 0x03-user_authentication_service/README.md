# User Authentication Service

## Description

This project implements a basic user authentication service using Python, Flask, and SQLAlchemy. The goal is to gain hands-on experience with fundamental concepts of authentication by building each component manually, including session handling, password hashing, and reset token management.

> **Note:** In real-world applications, always use production-grade libraries for authentication.

## Features

* User registration and login
* Secure password hashing using bcrypt
* Session management with cookies
* Password reset function
* RESTful API built with Flask

## Technologies Used

* Python 3.7
* Flask
* SQLAlchemy 1.3.x
* bcrypt
* SQLite (via SQLAlchemy ORM)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alx-backend-user-data.git
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

2. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

   Or manually install:

   ```bash
   pip3 install flask sqlalchemy==1.3 bcrypt
   ```

3. Run the Flask app:

   ```bash
   python3 app.py
   ```

## Usage

Use tools like `curl` or Postman to test API endpoints like:

* `POST /users` for registration
* `POST /sessions` for login
* `GET /profile` to fetch user profile
* `DELETE /sessions` to log out
* `POST /reset_password` and `PUT /reset_password` to handle password reset

## Project Structure

```
.
├── README.md
├── app.py
├── auth.py
├── db.py
├── user.py
├── main.py
└── a.db
```

## Author

This project is part of the ALX Backend specialization.

## License

This project is for educational purposes only. Not licensed for production use.
