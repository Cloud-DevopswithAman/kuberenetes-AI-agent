from app.core.kubectl import KubectlExecutor


def inspect_deployments(namespace: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace)
    result = executor.run(["get", "deployments", "-A"])

    if not result["success"]:
        return {"status": "error", "message": result["stderr"]}

    deployments = []
    for line in result["stdout"].splitlines()[1:]:
        parts = line.split()
        if len(parts) < 6:
            continue
        deployments.append(
            {
                "namespace": parts[0],
                "name": parts[1],
                "ready": parts[2],
                "up_to_date": parts[3],
                "available": parts[4],
                "age": parts[5],
            }
        )

    unhealthy = [d for d in deployments if d["available"] == "0" or d["ready"] != d["available"]]
    return {"status": "inspected", "deployments": deployments, "unhealthy": unhealthy}
