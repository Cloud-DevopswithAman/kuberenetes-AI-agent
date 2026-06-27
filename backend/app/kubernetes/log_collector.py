from app.core.kubectl import KubectlExecutor


def collect_logs(namespace: str | None = None, pod_name: str | None = None, context: str | None = None) -> dict:
    executor = KubectlExecutor(namespace=namespace, context=context)
    if not pod_name:
        return {"status": "skipped", "message": "No pod name provided"}

    result = executor.run(["logs", pod_name, "--tail=50"])
    if not result["success"]:
        return {"status": "error", "message": result["stderr"]}

    log_lines = [line for line in result["stdout"].splitlines() if line.strip()]
    relevant_lines = []
    keywords = ["error", "exception", "failed", "panic", "oom", "image", "connection"]

    for line in log_lines:
        lower = line.lower()
        if any(keyword in lower for keyword in keywords):
            relevant_lines.append(line)

    return {
        "status": "collected",
        "pod": pod_name,
        "relevant_lines": relevant_lines[:20],
    }
