from pydantic import BaseModel


class DiagnosisResponse(BaseModel):
    status: str = "pending"
    summary: str = "No investigation has been run yet."
    root_cause: str | None = None
    suggested_fix: str | None = None
