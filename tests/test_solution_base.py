import unittest
from unittest.mock import Mock
import random

from src.amcga.solution_base import AbstractSolution

class TestAbstractSolution(unittest.TestCase):
    def setUp(self):
        # Mock implementation of AbstractSolution
        class MockSolution(AbstractSolution):
            def calculate_fitness(self, fitness_function):
                self.fitness = fitness_function(self.value)

        self.solution = MockSolution(value=10)

    def test_initialization(self):
        self.assertEqual(self.solution.value, 10)
        self.assertEqual(self.solution.fitness, 0)

    def test_calculate_fitness(self):
        mock_fitness_function = Mock(return_value=42)
        self.solution.calculate_fitness(mock_fitness_function)
        self.assertEqual(self.solution.fitness, 42)
        mock_fitness_function.assert_called_once_with(10)

if __name__ == "__main__":
    unittest.main()
