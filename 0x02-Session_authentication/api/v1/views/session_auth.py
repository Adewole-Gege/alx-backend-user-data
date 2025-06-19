#!/usr/bin/env python3
""" Module for handling session authentication routes
"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
from api.v1.auth.session_auth import SessionAuth

session_auth = SessionAuth()


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ POST /auth_session/login
    Creates a session and returns user data + sets cookie
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = session_auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(session_auth.session_cookie_name, session_id)
    return response
