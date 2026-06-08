from __future__ import annotations

from typing import Protocol


class LLM(Protocol):
    async def generate(
        self,
        prompt: str,
    ) -> str: ...


class CognitiveOrganism:

    def __init__(
        self,
        llm: LLM,
        strategies: list[str],
    ):
        self.llm = llm
        self.strategies = strategies

    async def execute(
        self,
        task: str,
    ) -> str:

        prompt = f"""
Task:
{task}

Active Cognition:
{chr(10).join(self.strategies)}

Provide the best solution.
"""

        return await self.llm.generate(prompt)