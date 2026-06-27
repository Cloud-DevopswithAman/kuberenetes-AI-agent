from fastapi import APIRouter, Body, Header, HTTPException
from pydantic import BaseModel
from app.ai.reasoning.service import ReasoningService
from app.services.auth_service import get_user
from app.services.history_service import add_history
from app.services.investigation_service import run_investigation
from app.services.progress_service import update_progress


class InvestigateRequest(BaseModel):
    namespace: str | None = None
    context: str | None = None


router = APIRouter(prefix="/investigate", tags=["investigation"])
reasoning_service = ReasoningService()


def _get_current_user(authorization: str | None) -> dict | None:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    return get_user(token)


@router.post("")
def investigate(request: InvestigateRequest = Body(...), authorization: str | None = Header(None)) -> dict:
    user = _get_current_user(authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    investigation = run_investigation(namespace=request.namespace, context=request.context)
    progress_id = investigation.get("progress_id")

    if progress_id:
        update_progress(progress_id, "AI Reasoning", "running")

    diagnosis = reasoning_service.analyze(investigation)

    if progress_id:
        update_progress(progress_id, "AI Reasoning", "completed")
        update_progress(progress_id, "Diagnosis Complete", "completed")

    add_history({
        "user": user["username"],
        "namespace": request.namespace or "all",
        "context": request.context or "current",
        "root_cause": diagnosis.get("root_cause", "Unknown"),
        "confidence": diagnosis.get("confidence", 0),
        "status": "completed",
    })

    return {
        "status": "success",
        "investigation_id": progress_id,
        "context": request.context or "current",
        "investigation": investigation,
        "diagnosis": diagnosis,
    }
