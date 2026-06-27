from fastapi import APIRouter, Header, HTTPException
from app.services.auth_service import get_user
from app.services.history_service import get_history

router = APIRouter(prefix="/history", tags=["history"])


def _get_current_user(authorization: str | None) -> dict | None:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    return get_user(token)


@router.get("")
def history(authorization: str | None = Header(None)) -> dict:
    user = _get_current_user(authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"history": get_history()}
