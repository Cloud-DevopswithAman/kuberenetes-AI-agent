from app.core.kubectl import KubectlExecutor


def analyze_events(namespace: str | None = None, context: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace, context=context)
    command = ["get", "events", "--sort-by=.metadata.creationTimestamp"]
    if namespace is None:
        command.insert(2, "-A")
    result = executor.run(command)

    if not result["success"]:
        return {"status": "error", "message": result["stderr"]}

    findings = []
    keywords = ["FailedScheduling", "BackOff", "FailedMount", "FailedPull", "ErrImagePull", "Unhealthy"]

    for line in result["stdout"].splitlines()[1:]:
        if any(keyword in line for keyword in keywords):
            findings.append(line)

    return {"status": "analyzed", "findings": findings[:20]}
