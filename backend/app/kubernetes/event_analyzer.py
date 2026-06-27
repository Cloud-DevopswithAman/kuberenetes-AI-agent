from app.core.kubectl import KubectlExecutor


def analyze_events(namespace: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace)
    result = executor.run(["get", "events", "-A", "--sort-by=.metadata.creationTimestamp"])

    if not result["success"]:
        return {"status": "error", "message": result["stderr"]}

    findings = []
    keywords = ["FailedScheduling", "BackOff", "FailedMount", "FailedPull", "ErrImagePull", "Unhealthy"]

    for line in result["stdout"].splitlines()[1:]:
        if any(keyword in line for keyword in keywords):
            findings.append(line)

    return {"status": "analyzed", "findings": findings[:20]}
