from fastapi import APIRouter, Header, HTTPException
from app.core.kubectl import KubectlExecutor
from app.services.auth_service import get_user

router = APIRouter(prefix="/clusters", tags=["clusters"])


def _get_current_user(authorization: str | None) -> dict | None:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1]
    return get_user(token)


@router.get("")
def list_clusters(authorization: str | None = Header(None)) -> dict:
    user = _get_current_user(authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    executor = KubectlExecutor()
    result = executor.run(["config", "get-contexts", "-o", "name"])

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["stderr"] or "Unable to list clusters")

    contexts = [line.strip() for line in result["stdout"].splitlines() if line.strip()]
    current_context_result = executor.run(["config", "current-context"])
    current_context = current_context_result["stdout"].strip() if current_context_result["success"] else None

    return {
        "clusters": contexts,
        "current_context": current_context,
        "kubeconfig": executor.kubeconfig,
    }
