import unittest
from unittest.mock import Mock
import random

from src.amcga.adaptive_mutation import AbstractAdaptiveMutation

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
            p = max(0.01, min(abs(p), 1.0))
            self.assertGreaterEqual(p, 0.01)
            self.assertLessEqual(p, 1.0)

if __name__ == "__main__":
    unittest.main()