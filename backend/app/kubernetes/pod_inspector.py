from app.core.kubectl import KubectlExecutor


def inspect_pods(namespace: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace)
    result = executor.run(["get", "pods", "-A"])

    if not result["success"]:
        return {"healthy": False, "problematic_pods": [], "error": result["stderr"]}

    lines = [line for line in result["stdout"].splitlines() if line.strip()]
    problematic = []

    for line in lines[1:]:
        parts = line.split()
        if len(parts) < 3:
            continue
        name = parts[1]
        namespace_name = parts[0]
        status = parts[2] if len(parts) > 2 else "Unknown"
        if status in {
            "CrashLoopBackOff",
            "ImagePullBackOff",
            "Pending",
            "Error",
            "OOMKilled",
            "ContainerCreating",
        }:
            problematic.append(
                {
                    "name": name,
                    "namespace": namespace_name,
                    "status": status,
                }
            )

    return {"healthy": not problematic, "problematic_pods": problematic}
