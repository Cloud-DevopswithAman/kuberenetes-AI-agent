from app.core.kubectl import KubectlExecutor


def inspect_network(namespace: str | None = None, context: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace, context=context)
    svc_cmd = ["get", "svc"]
    ep_cmd = ["get", "endpoints"]
    if namespace is None:
        svc_cmd.append("-A")
        ep_cmd.append("-A")
    svc_result = executor.run(svc_cmd)
    ep_result = executor.run(ep_cmd)

    if not svc_result["success"]:
        return {"status": "error", "message": svc_result["stderr"]}

    services = svc_result["stdout"].splitlines()[1:]
    endpoints = ep_result["stdout"].splitlines()[1:]

    return {
        "status": "inspected",
        "services": services[:20],
        "endpoints": endpoints[:20],
    }
