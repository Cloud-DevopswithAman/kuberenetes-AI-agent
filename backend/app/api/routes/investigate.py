from fastapi import APIRouter
from app.services.investigation_service import run_investigation

router = APIRouter(prefix="/investigate", tags=["investigation"])


@router.post("")
def investigate() -> dict:
    return {
        "status": "success",
        "investigation": run_investigation(),
    }
