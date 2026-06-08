from __future__ import annotations

from typing import List

from pydantic import BaseModel

from app.genome.gene import Gene


class Genome(BaseModel):
    genome_id: str

    species: str

    generation: int = 1

    genes: List[Gene]

    def activate(self, task: str) -> List[Gene]:
        return [
            gene
            for gene in self.genes
            if gene.activate(task)
        ]

    def average_fitness(self) -> float:
        if not self.genes:
            return 0.0

        return (
            sum(g.fitness for g in self.genes)
            / len(self.genes)
        )