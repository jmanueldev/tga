from app.genome.gene import Gene
from app.genome.genome import Genome


def test_gene_activation():

    gene = Gene(
        trigger="research",
        strategy="search web"
    )

    assert gene.activate(
        "perform research on ai"
    )


def test_average_fitness():

    genome = Genome(
        genome_id="g1",
        species="research",
        genes=[
            Gene(
                trigger="a",
                strategy="x",
                fitness=0.5
            ),
            Gene(
                trigger="b",
                strategy="y",
                fitness=1.0
            ),
        ],
    )

    assert genome.average_fitness() == 0.75