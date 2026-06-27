from app.kubernetes.deployment_inspector import inspect_deployments
from app.kubernetes.event_analyzer import analyze_events
from app.kubernetes.log_collector import collect_logs
from app.kubernetes.network_inspector import inspect_network
from app.kubernetes.pod_inspector import inspect_pods


def run_investigation(namespace: str | None = None) -> dict:
    """Orchestrate a read-only Kubernetes investigation workflow."""
    pods = inspect_pods(namespace=namespace)
    logs = collect_logs(namespace=namespace, pod_name=None)
    events = analyze_events(namespace=namespace)
    deployments = inspect_deployments(namespace=namespace)
    network = inspect_network(namespace=namespace)

    return {
        "pods": pods,
        "logs": logs,
        "events": events,
        "deployments": deployments,
        "network": network,
    }
