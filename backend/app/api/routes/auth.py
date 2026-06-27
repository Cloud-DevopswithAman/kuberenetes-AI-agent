from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from app.services.auth_service import authenticate, get_user

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(request: LoginRequest) -> dict:
    session = authenticate(request.username, request.password)
    if not session:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": session["token"],
        "token_type": "bearer",
        "user": {"username": session["username"]},
    }


@router.get("/me")
def me(authorization: str | None = Header(None)) -> dict:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    user = get_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": user}
