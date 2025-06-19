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
0x02-Session_authentication/
├── README.md                             # ✅ REQUIRED by project spec
│                                         # Describes the project and setup
│                                         # [Project Requirement]
│
├── requirements.txt                      # ✅ REQUIRED by project spec
│                                         # Contains dependencies (e.g., Flask)
│                                         # [Copied from previous project]
│
├── api/
│   └── v1/
│       ├── __init__.py                   # ✅ Edit only if needed
│       │                                 # Registers Blueprints
│       │                                 # [Base project structure]
│       │
│       ├── app.py                        # ✅ MUST BE MODIFIED
│       │                                 # - Task 0: Assign `request.current_user`
│       │                                 # - Task 1: Switch to SessionAuth by env
│       │                                 # - Task 5: Add login path to excluded
│       │                                 # - Task 9, 10: Use SessionExpAuth/DBAuth
│       │
│       ├── views/
│       │   ├── __init__.py               # ✅ Edit to import session_auth view
│       │   │                             # - Task 7: Register session_auth route
│       │   │
│       │   ├── users.py                  # ✅ MUST BE MODIFIED
│       │   │                             # - Task 0: Handle `/users/me`
│       │   │
│       │   └── session_auth.py           # 🆕 MUST BE CREATED
│       │                                 # - Task 7: POST /auth_session/login
│       │                                 # - Task 8: DELETE /auth_session/logout
│
├── models/
│   ├── user.py                           # ✅ Already present from previous project
│   │                                     # Used for password validation and user retrieval
│   │
│   └── user_session.py                   # 🆕 MUST BE CREATED
│                                         # - Task 10: Store Session ID in DB
│
├── main_0.py to main_6.py                # ✅ Used for testing each task
│                                         # Task validation test scripts
│
├── main_100.py                           # ✅ Test for advanced Task 10
│
├── api/
│   └── v1/
│       └── auth/
│           ├── __init__.py               # ✅ From base project (no change expected)
│           │
│           ├── auth.py                   # ✅ MUST BE MODIFIED
│           │                             # - Task 4: Add session_cookie()
│           │
│           ├── basic_auth.py             # ✅ From previous project
│           │
│           ├── session_auth.py           # 🆕 MUST BE CREATED
│           │                             # - Task 1: Define empty SessionAuth
│           │                             # - Task 2: Add create_session()
│           │                             # - Task 3: Add user_id_for_session_id()
│           │                             # - Task 6: Add current_user()
│           │                             # - Task 8: Add destroy_session()
│           │
│           ├── session_exp_auth.py       # 🆕 MUST BE CREATED
│           │                             # - Task 9: Expiration support
│           │
│           └── session_db_auth.py        # 🆕 MUST BE CREATED
│                                         # - Task 10: DB-backed session storage
```
