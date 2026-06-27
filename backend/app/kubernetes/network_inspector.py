from app.core.kubectl import KubectlExecutor


def inspect_network(namespace: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace)
    svc_result = executor.run(["get", "svc", "-A"])
    ep_result = executor.run(["get", "endpoints", "-A"])

    if not svc_result["success"]:
        return {"status": "error", "message": svc_result["stderr"]}

    services = svc_result["stdout"].splitlines()[1:]
    endpoints = ep_result["stdout"].splitlines()[1:]

    return {
        "status": "inspected",
        "services": services[:20],
        "endpoints": endpoints[:20],
    }
