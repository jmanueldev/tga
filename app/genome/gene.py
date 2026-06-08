from __future__ import annotations

from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class Gene(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    trigger: str

    strategy: str

    fitness: float = 0.5

    mutation_rate: float = 0.05

    execution_count: int = 0

    success_count: int = 0

    def activate(self, context: str) -> bool:
        return self.trigger.lower() in context.lower()

    def reward(self, score: float) -> None:
        self.execution_count += 1
        self.success_count += 1
        self.fitness = min(1.0, self.fitness + score)

    def penalize(self, score: float) -> None:
        self.execution_count += 1
        self.fitness = max(0.0, self.fitness - score)