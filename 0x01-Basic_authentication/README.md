# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Stracture

```
0x01-Basic_authentication/                     # Project root directory
│
├── README.md                                  # ✅ REQUIRED: Project description (Mentioned in Requirements)
├── requirements.txt                           # ✅ REQUIRED: Contains dependencies to install (from archive.zip)
│
├── api/                                       # ✅ REQUIRED: Comes from archive.zip (Task 0)
│   └── v1/                                    # API version 1 structure
│       ├── __init__.py                        # Init module (archive content)
│       ├── app.py                             # ✅ Tasks 1, 2, 5, 6
│       │                                      # - Task 1: Add 401 handler
│       │                                      # - Task 2: Add 403 handler
│       │                                      # - Task 5: Add before_request auth checks
│       │                                      # - Task 6: Use BasicAuth depending on AUTH_TYPE
│       └── views/                             # Views (endpoints)
│           ├── __init__.py                    # View package initializer
│           ├── index.py                       # ✅ Tasks 1, 2
│           │                                  # - Task 1: /unauthorized → abort(401)
│           │                                  # - Task 2: /forbidden → abort(403)
│           └── users.py                       # Default endpoint file (archive content, used in tests)
│
├── models/                                    # ✅ REQUIRED: Comes from archive.zip (User management)
│   ├── __init__.py                            # Module initializer
│   ├── base_model.py                          # Likely base class for models
│   ├── user.py                                # ✅ Task 10 (user auth logic)
│   └── ...                                    # Possibly storage handlers (file_storage.py etc.)
│
└── api/v1/auth/                               # ✅ Tasks 3–13: Authentication logic
    ├── __init__.py                            # Init file for auth package (Task 3)
    ├── auth.py                                # ✅ Tasks 3, 4, 5, 13
    │                                          # - Task 3: Define Auth base class
    │                                          # - Task 4: Implement require_auth with / logic
    │                                          # - Task 5: Add authorization_header
    │                                          # - Task 13: Add wildcard path (*) support
    └── basic_auth.py                          # ✅ Tasks 6–12
                                               # - Task 6: Create BasicAuth class
                                               # - Task 7: extract_base64_authorization_header
                                               # - Task 8: decode_base64_authorization_header
                                               # - Task 9: extract_user_credentials
                                               # - Task 10: user_object_from_credentials
                                               # - Task 11: current_user override
                                               # - Task 12: support ":" in passwords
```
