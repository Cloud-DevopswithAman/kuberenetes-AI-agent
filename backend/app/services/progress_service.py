from typing import Any

PROGRESS: dict[str, dict[str, Any]] = {}
STEPS = [
    "Checking Pods",
    "Reading Logs",
    "Analyzing Events",
    "Inspecting Deployments",
    "Checking Networking",
    "AI Reasoning",
    "Diagnosis Complete",
]


def create_progress() -> str:
    import uuid

    progress_id = str(uuid.uuid4())
    PROGRESS[progress_id] = {
        "id": progress_id,
        "steps": [{"name": name, "status": "pending"} for name in STEPS],
        "started_at": None,
        "completed": False,
    }
    return progress_id


def update_progress(progress_id: str, step_name: str, status: str) -> None:
    progress = PROGRESS.get(progress_id)
    if not progress:
        return

    if progress["started_at"] is None:
        progress["started_at"] = "running"

    for step in progress["steps"]:
        if step["name"] == step_name:
            step["status"] = status
            break

    if step_name == "Diagnosis Complete" and status == "completed":
        progress["completed"] = True


def get_progress(progress_id: str) -> dict[str, Any] | None:
    return PROGRESS.get(progress_id)
