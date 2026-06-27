from typing import Any


def build_prompt(investigation: dict[str, Any]) -> str:
    pods = investigation.get("pods", {})
    logs = investigation.get("logs", {})
    events = investigation.get("events", {})
    deployments = investigation.get("deployments", {})
    network = investigation.get("network", {})

    return f"""
You are a Senior Kubernetes SRE.

Analyze the following troubleshooting evidence and return a concise incident diagnosis.

Pod Status:
{pods}

Logs:
{logs}

Events:
{events}

Deployment Health:
{deployments}

Networking Findings:
{network}

Return the result as JSON with these fields:
1. root_cause
2. explanation
3. fix
4. kubectl_command
5. prevention_recommendation
6. confidence
"""
