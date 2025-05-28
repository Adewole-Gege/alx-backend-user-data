# 0x00. Personal data

## Description

This project focuses on handling Personally Identifiable Information (PII) safely through logging and database access, with emphasis on:

- Obfuscating sensitive log fields
- Hashing and validating passwords
- Connecting to a secure MySQL database using environment variables
- Implementing secure log formatters

## Files

- `filtered_logger.py`: Implements logging utilities and secure DB connection
- `encrypt_password.py`: Implements password hashing and validation

## Requirements

- Python 3.7+
- `mysql-connector-python` for DB access
- `bcrypt` for password hashing

## Usage

Make sure to set the following environment variables for DB access:

```bash
export PERSONAL_DATA_DB_USERNAME='root'
export PERSONAL_DATA_DB_PASSWORD='yourpassword'
export PERSONAL_DATA_DB_HOST='localhost'
export PERSONAL_DATA_DB_NAME='my_db'
```
