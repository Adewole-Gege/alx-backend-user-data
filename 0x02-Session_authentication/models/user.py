#!/usr/bin/env python3
"""User model."""
import uuid
from datetime import datetime
from models import storage
from hashlib import md5


class User:
    """A minimal User model storing email & hashed password."""

    def __init__(self, *args, **kwargs):
        """Create new or load from kwargs dict."""
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    # ---------------- Password helpers ---------------- #
    @property
    def password(self):
        """Password getter (hash is stored)."""
        return self._password

    @password.setter
    def password(self, pwd):
        """Hash password on set."""
        self._password = md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd: str) -> bool:
        """Check plaintext password against stored hash."""
        return self._password == md5(pwd.encode()).hexdigest()

    # ---------------- Storage helpers ----------------- #
    def save(self):
        """Save/update object to storage."""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_json(self, save_to_file=False):
        """Return dict representation for JSON serialization."""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        # hide hashed pwd when sending to client
        if not save_to_file:
            d.pop("_password", None)
        return d

    # ---------------- Class helpers ------------------- #
    @classmethod
    def get(cls, user_id: str):
        """Retrieve a user by ID."""
        objs = storage.all(cls)
        key = "{}.{}".format(cls.__name__, user_id)
        return objs.get(key)

    @classmethod
    def search(cls, attrs: dict):
        """Naive search by attributes (supports only email for this project)."""
        result = []
        for obj in storage.all(cls).values():
            match = all(getattr(obj, k) == v for k, v in attrs.items())
            if match:
                result.append(obj)
        return result
