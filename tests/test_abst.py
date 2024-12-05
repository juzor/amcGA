import unittest
from unittest.mock import Mock
import random

from src.amcga.abst import AbstractSolution, AbstractChangeDetection, AbstractAdaptiveMutation

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


class TestAbstractChangeDetection(unittest.TestCase):
    def setUp(self):
        # Mock implementation of AbstractChangeDetection
        class MockChangeDetection(AbstractChangeDetection):
            def change_detection(self):
                return self.dfitness > self.variance

        self.change_detection = MockChangeDetection(dfitness=0.5, mean=1, variance=0.3)

    def test_initialization(self):
        self.assertEqual(self.change_detection.dfitness, 0.5)
        self.assertEqual(self.change_detection.mean, 1)
        self.assertEqual(self.change_detection.variance, 0.3)

    def test_change_detection(self):
        self.assertTrue(self.change_detection.change_detection())


class TestAbstractAdaptiveMutation(unittest.TestCase):
    def setUp(self):
        # Mock implementation of AbstractAdaptiveMutation
        class MockAdaptiveMutation(AbstractAdaptiveMutation):
            def prob_mut(self):
                return super().prob_mut()

            def am1(self, pm):
                super().am1(pm)

            def am2(self, pm):
                super().am2(pm)

            def am3(self, pm):
                super().am3(pm)

        self.adaptive_mutation = MockAdaptiveMutation(
            cd=0.4, m_pv=[0.2, 0.4, 0.6], ml=0.01, mh=0.5, dl=0.0, dh=1.0
        )

    def test_initialization(self):
        self.assertEqual(self.adaptive_mutation.cd, 0.4)
        self.assertEqual(self.adaptive_mutation.m_pv, [0.2, 0.4, 0.6])
        self.assertEqual(self.adaptive_mutation.ml, 0.01)
        self.assertEqual(self.adaptive_mutation.mh, 0.5)
        self.assertEqual(self.adaptive_mutation.dl, 0.0)
        self.assertEqual(self.adaptive_mutation.dh, 1.0)

    def test_prob_mut(self):
        pm = self.adaptive_mutation.prob_mut()
        self.assertGreaterEqual(pm, 0.01)
        self.assertLessEqual(pm, 0.5)

    def test_am1(self):
        pm = self.adaptive_mutation.prob_mut()
        self.adaptive_mutation.am1(pm)
        # Ensure m_pv values are within expected range
        for p in self.adaptive_mutation.m_pv:
            self.assertGreaterEqual(p, 0.01)
            self.assertLessEqual(p, 1.0)

    def test_am2(self):
        pm = self.adaptive_mutation.prob_mut()
        self.adaptive_mutation.am2(pm)
        # Ensure m_pv values are within expected range
        for p in self.adaptive_mutation.m_pv:
            self.assertGreaterEqual(p, 0.01)
            self.assertLessEqual(p, 1.0)

    def test_am3(self):
        pm = self.adaptive_mutation.prob_mut()
        self.adaptive_mutation.am3(pm)
        # Ensure m_pv values are within expected range
        for p in self.adaptive_mutation.m_pv:
            self.assertGreaterEqual(p, 0.01)
            self.assertLessEqual(p, 1.0)


if __name__ == "__main__":
    unittest.main()
