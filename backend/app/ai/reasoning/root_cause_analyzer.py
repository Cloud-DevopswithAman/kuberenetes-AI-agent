from typing import Any


def analyze_root_cause(investigation: dict[str, Any]) -> dict[str, Any]:
    pods = investigation.get("pods", {})
    logs = investigation.get("logs", {})
    events = investigation.get("events", {})
    deployments = investigation.get("deployments", {})
    network = investigation.get("network", {})

    if pods.get("healthy") is False:
        return {
            "root_cause": "Pods are unhealthy or in a failing state.",
            "explanation": "The investigation found unhealthy pod states that need attention.",
            "fix": "Inspect the failing pod and its workload definition.",
            "kubectl_command": "kubectl get pods -A",
            "prevention_recommendation": "Review pod readiness and restart policies.",
            "confidence": 70,
        }

    if events.get("status") == "error":
        return {
            "root_cause": "Kubernetes events indicate a cluster-level issue.",
            "explanation": "Recent events suggest an operational problem that needs follow-up.",
            "fix": "Check recent events and resource conditions.",
            "kubectl_command": "kubectl get events -A",
            "prevention_recommendation": "Monitor event trends and resource constraints.",
            "confidence": 60,
        }

    return {
        "root_cause": "No obvious failure pattern detected.",
        "explanation": "The investigation did not reveal a clear issue from the current evidence.",
        "fix": "Inspect cluster resources manually for further signs of trouble.",
        "kubectl_command": "kubectl get all -A",
        "prevention_recommendation": "Collect more evidence before making changes.",
        "confidence": 40,
    }
