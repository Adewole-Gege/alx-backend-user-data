#!/usr/bin/env python3
"""
Module for filtering log messages that may contain personal data.
"""
import re
import logging
from typing import List
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.
    """
    return re.sub(
        fr"({'|'.join(fields)})=.+?{separator}",
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering PII fields from log messages.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using filter_datum.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION,
            record.getMessage(), self.SEPARATOR
        )
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Returns a configured logger that filters PII fields.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a secure MySQL database using environment variables.
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """
    Retrieves and logs all rows from the users table
    with PII fields obfuscated.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = "; ".join(
            f"{desc[0]}={str(value)}"
            for desc, value in zip(cursor.description, row)
        ) + ";"
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
