#!/usr/bin/env python3
""" Main application module for API v1
"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage
from api.v1.auth.auth import Auth

auth = None
auth_type = getenv("AUTH_TYPE")

# Dynamically import based on AUTH_TYPE
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif auth_type == "session_db_auth":
    from api.v1.auth.session_db_auth import SessionDBAuth
    auth = SessionDBAuth()
else:
    auth = Auth()

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown(exception):
    """ Close storage """
    storage.close()

@app.before_request
def before_request():
    """ Executed before each request """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check if authorization or session cookie is present
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)

    user = auth.current_user(request)
    if user is None:
        abort(403)

    request.current_user = user

@app.errorhandler(401)
def unauthorized(error):
    """ Handle 401 Unauthorized """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """ Handle 403 Forbidden """
    return jsonify({"error": "Forbidden"}), 403

@app.errorhandler(404)
def not_found(error):
    """ Handle 404 Not Found """
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
