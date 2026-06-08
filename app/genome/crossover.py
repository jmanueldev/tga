from __future__ import annotations

from app.genome.genome import Genome


class GenomeCrossover:

    def crossover(
        self,
        parent_a: Genome,
        parent_b: Genome,
        child_id: str,
    ) -> Genome:

        midpoint_a = len(parent_a.genes) // 2
        midpoint_b = len(parent_b.genes) // 2

        genes = (
            parent_a.genes[:midpoint_a]
            + parent_b.genes[midpoint_b:]
        )

        return Genome(
            genome_id=child_id,
            species=parent_a.species,
            generation=max(
                parent_a.generation,
                parent_b.generation,
            )
            + 1,
            genes=genes,
        )