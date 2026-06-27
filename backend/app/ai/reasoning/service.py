from typing import Any

from app.ai.reasoning.confidence_engine import score_confidence
from app.ai.reasoning.llm_client import LLMClient
from app.ai.reasoning.prompt_builder import build_prompt
from app.ai.reasoning.root_cause_analyzer import analyze_root_cause


class ReasoningService:
    def __init__(self) -> None:
        self.llm_client = LLMClient()

    def analyze(self, investigation: dict[str, Any]) -> dict[str, Any]:
        prompt = build_prompt(investigation)
        llm_result = self.llm_client.generate(prompt)

        if llm_result.get("root_cause") == "OpenRouter API key not configured":
            fallback = analyze_root_cause(investigation)
            fallback["confidence"] = score_confidence(fallback, investigation)
            return fallback

        llm_result["confidence"] = score_confidence(llm_result, investigation)
        return llm_result
