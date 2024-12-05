"""
import key modules
"""

from abc import ABC, abstractmethod
import random


class AbstractSolution(ABC):
    """
    Abstract base class for representing a solution in an optimization problem.
    Attributes:
        value: The solution's representation (e.g., binary string, array).
        fitness: The fitness value of the solution.
    """

    def __init__(self, value):
        """
        Initializes the solution with a value and a default fitness of 0.

        Args:
            value: The representation of the solution.
        """
        self.value = value
        self.fitness = 0

    @abstractmethod
    def calculate_fitness(self, fitness_function):
        """
        Abstract method to calculate the fitness of the solution.

        Args:
            fitness_function: A callable that takes the solution's
            value and returns a fitness score.
        """
        pass


class AbstractChangeDetection(ABC):
    """
    Abstract base class for detecting changes in fitness over time.

    Attributes:
        dfitness: The fitness difference threshold for detecting changes.
        mean: The mean value for fitness variation detection.
        variance: The variance threshold for fitness variation detection.
    """

    def __init__(self, dfitness, mean=1, variance=0.3):
        """
        Initializes change detection with specified thresholds.

        Args:
            dfitness: Fitness change threshold.
            mean: Mean value for change detection.
            variance: Variance threshold for change detection.
        """
        self.dfitness = dfitness
        self.mean = mean
        self.variance = variance

    @abstractmethod
    def change_detection(self):
        """
        Abstract method to implement fitness change detection logic.
        """
        pass


class AbstractAdaptiveMutation(ABC):
    """
    Abstract base class for adaptive mutation strategies in genetic algorithms.

    Attributes:
        ml: Minimum mutation probability.
        mh: Maximum mutation probability.
        dl: Minimum detection threshold.
        dh: Maximum detection threshold.
        cd: Current detection value.
        m_pv: Probability vector for adaptive mutation.
    """

    def __init__(self, cd, m_pv, ml=0.01, mh=0.5, dl=0.0, dh=1.0):
        """
        Initializes adaptive mutation with specified parameters.

        Args:
            cd: Current detection value.
            m_pv: Probability vector for mutation.
            ml: Minimum mutation probability.
            mh: Maximum mutation probability.
            dl: Minimum detection threshold.
            dh: Maximum detection threshold.
        """
        self.ml = ml
        self.mh = mh
        self.dl = dl
        self.dh = dh
        self.cd = cd
        self.m_pv = m_pv

    @abstractmethod
    def prob_mut(self):
        """
        Calculates the mutation probability based on adaptive parameters.

        Returns:
            The mutation probability (clipped to the range [0.01, 0.5]).
        """
        pm = self.ml + (self.cd - self.dl) * ((self.mh - self.ml) / (self.dh - self.dl))
        return max(0.01, min(pm, 0.5))  # Clip pm to the range [0.01, 0.5]

    @abstractmethod
    def am1(self, pm):
        """
        Adaptive mutation method 1: Random mutation based on pm.

        Args:
            pm: Mutation probability.
        """
        r = random.random()
        for i in range(len(self.m_pv)):
            self.m_pv[i] = (
                random.uniform(self.cd, self.m_pv[i]) if r < pm else self.m_pv[i]
            )

    @abstractmethod
    def am2(self, pm):
        """
        Adaptive mutation method 2: Adjusts probabilities using |r - pm|.

        Args:
            pm: Mutation probability.
        """
        r = random.random()
        for i in range(len(self.m_pv)):
            self.m_pv[i] = abs(self.m_pv[i] + (r - pm)) if r < pm else self.m_pv[i]

    @abstractmethod
    def am3(self, pm):
        """
        Adaptive mutation method 3: Weighted adjustment based on pm.

        Args:
            pm: Mutation probability.
        """
        r = random.random()
        adjustment = (r - pm) / 2
        for i in range(len(self.m_pv)):
            self.m_pv[i] = (
                self.m_pv[i] + adjustment if r < pm else self.m_pv[i] - adjustment
            )
