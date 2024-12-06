import unittest
from unittest.mock import MagicMock, create_autospec
import math
from src.amcga.change_detection import AbstractChangeDetection

class TestAbstractChangeDetectionWithMock(unittest.TestCase):
    def setUp(self):
        # Create a mock subclass of AbstractChangeDetection
        self.mock_change_detection = create_autospec(AbstractChangeDetection, instance=True)
        self.mock_change_detection.sigma = 0.1
        self.mock_change_detection.c = 1

        # Mock the abstract method 'detect_change'
        self.mock_change_detection.detect_change = MagicMock(return_value=True)

    def test_calculate_fitness_change(self):
        # Test the calculate_fitness_change method
        self.mock_change_detection.calculate_fitness_change = AbstractChangeDetection.calculate_fitness_change
        result = self.mock_change_detection.calculate_fitness_change(None, 0.95, 0.92)
        self.assertAlmostEqual(result, 0.03)

    def test_calculate_a(self):
        # Test the calculate_a method
        self.mock_change_detection.sigma = 0.1  # Set sigma value
        self.mock_change_detection.c = 1       # Set c value
        self.mock_change_detection.calculate_a = AbstractChangeDetection.calculate_a

        # Pass self as the mock object itself, along with delta_f
        delta_f = 0.03
        result = self.mock_change_detection.calculate_a(self.mock_change_detection, delta_f)
        expected_a = ((delta_f - self.mock_change_detection.c) ** 2) / (2 * (self.mock_change_detection.sigma ** 2))
        self.assertAlmostEqual(result, expected_a)


    def test_calculate_cd(self):
        # Test the calculate_cd method
        self.mock_change_detection.calculate_cd = AbstractChangeDetection.calculate_cd
        a = 5
        result = self.mock_change_detection.calculate_cd(None, a)
        self.assertAlmostEqual(result, math.exp(-a))

    def test_detect_change_mock(self):
        # Test the mocked detect_change method
        result = self.mock_change_detection.detect_change(0.95, 0.92)
        self.mock_change_detection.detect_change.assert_called_once_with(0.95, 0.92)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
