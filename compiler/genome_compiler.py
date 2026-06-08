from app.genome.genome import Genome


class GenomeCompiler:

    def compile(
        self,
        genome: Genome,
        task: str,
    ) -> list[str]:

        active_genes = genome.activate(task)

        strategies = []

        for gene in active_genes:
            strategies.append(gene.strategy)

        return strategies