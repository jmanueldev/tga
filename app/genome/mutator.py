from __future__ import annotations

import random

from app.genome.genome import Genome


class GenomeMutator:

    STRATEGY_MUTATIONS = [
        "verify answer before responding",
        "simulate 3 futures",
        "self critique reasoning",
        "run adversarial review",
        "perform uncertainty estimation",
    ]

    def mutate(self, genome: Genome) -> Genome:

        if not genome.genes:
            return genome

        gene = random.choice(genome.genes)

        mutation = random.choice(
            self.STRATEGY_MUTATIONS
        )

        gene.strategy += f"\n{mutation}"

        gene.mutation_rate *= 1.05

        return genome