import logging
import subprocess
from typing import Any

logger = logging.getLogger(__name__)


class KubectlExecutor:
    def __init__(self, namespace: str | None = None) -> None:
        self.namespace = namespace

    def run(self, command: list[str]) -> dict[str, Any]:
        try:
            if self.namespace:
                command = command[:1] + ["-n", self.namespace] + command[1:]

            completed = subprocess.run(
                ["kubectl", *command],
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )

            return {
                "success": completed.returncode == 0,
                "returncode": completed.returncode,
                "stdout": completed.stdout.strip(),
                "stderr": completed.stderr.strip(),
            }
        except FileNotFoundError:
            logger.exception("kubectl executable not found")
            return {
                "success": False,
                "returncode": 127,
                "stdout": "",
                "stderr": "kubectl executable not found",
            }
        except subprocess.TimeoutExpired:
            logger.exception("kubectl command timed out")
            return {
                "success": False,
                "returncode": 124,
                "stdout": "",
                "stderr": "kubectl command timed out",
            }
