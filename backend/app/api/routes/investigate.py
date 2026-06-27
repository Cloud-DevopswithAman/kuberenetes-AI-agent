from fastapi import APIRouter
from app.ai.reasoning.service import ReasoningService
from app.services.investigation_service import run_investigation

router = APIRouter(prefix="/investigate", tags=["investigation"])
reasoning_service = ReasoningService()


@router.post("")
def investigate() -> dict:
    investigation = run_investigation()
    diagnosis = reasoning_service.analyze(investigation)

    return {
        "status": "success",
        "investigation": investigation,
        "diagnosis": diagnosis,
    }
