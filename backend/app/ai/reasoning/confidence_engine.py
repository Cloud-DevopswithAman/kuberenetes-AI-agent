from typing import Any


def score_confidence(analysis: dict[str, Any], investigation: dict[str, Any]) -> int:
    score = 50
    pods = investigation.get("pods", {})
    logs = investigation.get("logs", {})
    events = investigation.get("events", {})
    deployments = investigation.get("deployments", {})

    if pods.get("healthy") is False:
        score += 20
    if logs.get("status") == "collected":
        score += 10
    if events.get("status") == "analyzed":
        score += 10
    if deployments.get("status") == "inspected":
        score += 10

    return min(score, 95)
