from dataclasses import dataclass


@dataclass(slots=True)
class FitnessInput:
    accuracy: float
    latency: float
    cost_efficiency: float
    robustness: float
    safety: float


class FitnessCalculator:

    @staticmethod
    def score(metrics: FitnessInput) -> float:

        score = (
            metrics.accuracy * 0.40
            + metrics.robustness * 0.20
            + metrics.cost_efficiency * 0.15
            + metrics.latency * 0.15
            + metrics.safety * 0.10
        )

        return round(score, 4)