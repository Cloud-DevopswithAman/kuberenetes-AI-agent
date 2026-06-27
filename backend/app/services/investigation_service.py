from app.kubernetes.deployment_inspector import inspect_deployments
from app.kubernetes.event_analyzer import analyze_events
from app.kubernetes.log_collector import collect_logs
from app.kubernetes.network_inspector import inspect_network
from app.kubernetes.pod_inspector import inspect_pods
from app.services.progress_service import create_progress, update_progress


def run_investigation(namespace: str | None = None, context: str | None = None) -> dict:
    """Orchestrate a read-only Kubernetes investigation workflow."""
    progress_id = create_progress()

    update_progress(progress_id, "Checking Pods", "running")
    pods = inspect_pods(namespace=namespace, context=context)
    update_progress(progress_id, "Checking Pods", "completed")

    failed_pod_name = None
    if pods.get("problematic_pods"):
        failed_pod_name = pods["problematic_pods"][0].get("name")

    update_progress(progress_id, "Reading Logs", "running")
    logs = collect_logs(namespace=namespace, pod_name=failed_pod_name, context=context)
    update_progress(progress_id, "Reading Logs", "completed")

    update_progress(progress_id, "Analyzing Events", "running")
    events = analyze_events(namespace=namespace, context=context)
    update_progress(progress_id, "Analyzing Events", "completed")

    update_progress(progress_id, "Inspecting Deployments", "running")
    deployments = inspect_deployments(namespace=namespace, context=context)
    update_progress(progress_id, "Inspecting Deployments", "completed")

    update_progress(progress_id, "Checking Networking", "running")
    network = inspect_network(namespace=namespace, context=context)
    update_progress(progress_id, "Checking Networking", "completed")

    return {
        "progress_id": progress_id,
        "pods": pods,
        "logs": logs,
        "events": events,
        "deployments": deployments,
        "network": network,
    }
