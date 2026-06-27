import logging
import os
import subprocess
from typing import Any

logger = logging.getLogger(__name__)


class KubectlExecutor:
    def __init__(self, namespace: str | None = None, context: str | None = None) -> None:
        self.namespace = namespace
        self.context = context
        self.kubeconfig = os.getenv("KUBECONFIG_PATH", os.getenv("KUBECONFIG", "")) or None

    def run(self, command: list[str]) -> dict[str, Any]:
        try:
            kubectl_command = ["kubectl"]
            if self.kubeconfig:
                kubectl_command.extend(["--kubeconfig", self.kubeconfig])
            if self.context:
                kubectl_command.extend(["--context", self.context])
            if self.namespace and command[0] != "config" and "-A" not in command and "--all-namespaces" not in command:
                command = command[:1] + ["-n", self.namespace] + command[1:]

            completed = subprocess.run(
                [*kubectl_command, *command],
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )

            stderr = completed.stderr.strip()
            hint = self._build_hint(stderr)

            return {
                "success": completed.returncode == 0,
                "returncode": completed.returncode,
                "stdout": completed.stdout.strip(),
                "stderr": stderr,
                "hint": hint,
            }
        except FileNotFoundError:
            logger.exception("kubectl executable not found")
            return {
                "success": False,
                "returncode": 127,
                "stdout": "",
                "stderr": "kubectl executable not found",
                "hint": "Install kubectl and make sure it is available in PATH.",
            }
        except subprocess.TimeoutExpired:
            logger.exception("kubectl command timed out")
            return {
                "success": False,
                "returncode": 124,
                "stdout": "",
                "stderr": "kubectl command timed out",
                "hint": "The cluster may be unreachable or slow to respond.",
            }

    def _build_hint(self, stderr: str) -> str:
        if "No such file or directory" in stderr or "The system cannot find the path specified" in stderr:
            return "Verify the KUBECONFIG_PATH environment variable and kubeconfig file path."
        if "Unable to connect to the server" in stderr or "connection refused" in stderr.lower():
            return "Unable to connect to the Kubernetes API server. Check cluster access and network connectivity."
        if "* current-context" in stderr or "no configuration has been provided" in stderr.lower():
            return "Ensure kubectl is configured with a valid kubeconfig and current context."
        return ""
