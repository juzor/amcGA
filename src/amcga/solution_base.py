"""
import key modules
"""

from abc import ABC, abstractmethod


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
