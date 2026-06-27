import os
import logging
from typing import Any
import httpx

logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENROUTER_API_KEY", "")
        self.model = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt: str) -> dict[str, Any]:
        if not self.api_key:
            return {
                "root_cause": "OpenRouter API key not configured",
                "explanation": "AI reasoning is unavailable because no API key was provided.",
                "fix": "Set OPENROUTER_API_KEY and retry.",
                "kubectl_command": "",
                "prevention_recommendation": "Configure the environment variable for the AI layer.",
                "confidence": 0,
            }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a Senior Kubernetes SRE."},
                {"role": "user", "content": prompt},
            ],
        }

        try:
            with httpx.Client(timeout=20.0) as client:
                response = client.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                )
                response.raise_for_status()
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                return self._parse_content(content)
        except Exception as exc:
            logger.exception("LLM request failed")
            return {
                "root_cause": "AI reasoning failed",
                "explanation": str(exc),
                "fix": "Check the OpenRouter configuration and network access.",
                "kubectl_command": "",
                "prevention_recommendation": "Verify API credentials and connectivity.",
                "confidence": 0,
            }

    def _parse_content(self, content: str) -> dict[str, Any]:
        try:
            import json

            return json.loads(content)
        except Exception:
            return {
                "root_cause": "Unable to parse model response",
                "explanation": content,
                "fix": "Review the model response format.",
                "kubectl_command": "",
                "prevention_recommendation": "Ensure the model returns structured JSON.",
                "confidence": 0,
            }
