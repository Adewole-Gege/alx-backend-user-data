#!/usr/bin/env python3
"""Session authentication module
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
import os


class SessionAuth(Auth):
    """Session Authentication class"""

    user_id_by_session_id = {}

    def __init__(self):
        """Initialize with session cookie name"""
        super().__init__()
        self.session_cookie_name = os.getenv("SESSION_NAME", "_my_session_id")

    def create_session(self, user_id=None):
        """Create a session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve user ID based on session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return User instance based on session cookie"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
