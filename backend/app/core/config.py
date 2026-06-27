import os
from functools import lru_cache


@lru_cache(maxsize=1)
def get_settings() -> dict:
    return {
        "openrouter_api_key": os.getenv("OPENROUTER_API_KEY", ""),
        "openrouter_model": os.getenv("OPENROUTER_MODEL", "gpt-4o-mini"),
        "kubeconfig_path": os.getenv("KUBECONFIG_PATH", ""),
    }
