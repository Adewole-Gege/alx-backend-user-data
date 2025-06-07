#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import TypeVar, Dict, Any


class DB:
    """DB class for interacting with the database"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """Find the first user matching the given filter criteria"""
        if not kwargs:
            raise InvalidRequestError("No search parameters provided")
        query = self._session.query(User)
        for key in kwargs:
            if not hasattr(User, key):
                raise InvalidRequestError(f"Invalid field: {key}")
        user = query.filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound("No user found")
        return user

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """Update a user with given fields by their user_id"""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)
        self._session.commit()
