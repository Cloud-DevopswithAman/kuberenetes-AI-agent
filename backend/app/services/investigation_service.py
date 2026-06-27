from app.kubernetes.inspect import inspect_deployments, inspect_pods


def run_investigation() -> dict:
    """Placeholder service for orchestrating investigation."""
    inspect_pods()
    inspect_deployments()
    return {"status": "initialized", "message": "Investigation flow ready"}
