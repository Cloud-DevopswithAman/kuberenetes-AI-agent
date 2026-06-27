from fastapi import APIRouter, Header, HTTPException
from app.services.auth_service import get_user
from app.services.progress_service import get_progress

router = APIRouter(prefix="/progress", tags=["progress"])


def _get_current_user(authorization: str | None) -> dict | None:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    return get_user(token)


@router.get("/{progress_id}")
def progress(progress_id: str, authorization: str | None = Header(None)) -> dict:
    user = _get_current_user(authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    progress_data = get_progress(progress_id)
    if progress_data is None:
        raise HTTPException(status_code=404, detail="Progress not found")
    return {"progress": progress_data}
