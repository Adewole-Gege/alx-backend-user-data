#!/usr/bin/env python3
""" Authentication module for API
"""
import os
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """ Base class for all authentication systems """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Supports wildcard * at the end of excluded paths.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize path to always end with slash
        if not path.endswith('/'):
            path += '/'

        for ex_path in excluded_paths:
            if ex_path.endswith('*'):
                # Match prefix for wildcard
                if path.startswith(ex_path[:-1]):
                    return False
            elif path == ex_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header from request
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user (default None)
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns the value of the session cookie from the request
        """
        if request is None:
            return None
        cookie_name = os.getenv("SESSION_NAME")
        if cookie_name is None:
            return None
        return request.cookies.get(cookie_name)
