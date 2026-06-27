from datetime import datetime
from typing import Any

HISTORY: list[dict[str, Any]] = []


def add_history(record: dict[str, Any]) -> None:
    HISTORY.insert(0, {"timestamp": datetime.utcnow().isoformat() + "Z", **record})
    if len(HISTORY) > 20:
        HISTORY.pop()


def get_history() -> list[dict[str, Any]]:
    return HISTORY
