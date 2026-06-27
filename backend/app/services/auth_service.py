import uuid
from datetime import datetime, timedelta
from typing import Any

SESSIONS: dict[str, dict[str, Any]] = {}


def authenticate(username: str, password: str) -> dict[str, Any]:
    if not username or not password:
        return {}

    token = str(uuid.uuid4())
    session = {
        "token": token,
        "username": username,
        "expires_at": datetime.utcnow() + timedelta(hours=8),
    }
    SESSIONS[token] = session
    return session


def get_user(token: str | None) -> dict[str, Any] | None:
    if not token:
        return None

    session = SESSIONS.get(token)
    if not session:
        return None

    if session["expires_at"] < datetime.utcnow():
        del SESSIONS[token]
        return None

    return {"username": session["username"]}
