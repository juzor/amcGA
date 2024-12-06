from abc import ABC, abstractmethod
import math


class AbstractChangeDetection(ABC):
    """
    Abstract class for implementing change detection in fitness functions.
    Provides default implementations for calculating fitness change (Δf),
    intermediate value (a), and change detection probability (cd).
    """

    def __init__(self, sigma=0.3, c=1):
        """
        Initialize the default parameters for change detection.

        Parameters:
            sigma (float): Standard deviation for the change detection equation. Default is 0.1.
            c (float): Mean value for the change detection equation. Default is 1.
        """
        self.sigma = sigma
        self.c = c

    def calculate_fitness_change(self, f_t_minus_1, f_t):
        """
        Calculate the fitness change (Δf) as the difference between fitness values.

        Parameters:
            f_t_minus_1 (float): Fitness value at generation t-1.
            f_t (float): Fitness value at generation t.

        Returns:
            float: The calculated fitness change (Δf).
        """
        return f_t_minus_1 - f_t

    def calculate_a(self, delta_f):
        """
        Calculate the intermediate value 'a' using the fitness change, mean, and standard deviation.

        Parameters:
            delta_f (float): Change in fitness (Δf).

        Returns:
            float: The computed value of 'a'.
        """
        return ((delta_f - self.c) ** 2) / (2 * self.sigma**2)

    def calculate_cd(self, a):
        """
        Calculate the change detection probability (cd) using the intermediate value 'a'.

        Parameters:
            a (float): Intermediate value computed from the fitness change equation.

        Returns:
            float: The change detection probability (cd).
        """
        return math.exp(-a)

    @abstractmethod
    def detect_change(self, f_t_minus_1, f_t):
        """
        Abstract method for detecting change based on fitness values.

        Subclasses must implement this method to define their own logic.

        Parameters:
            f_t_minus_1 (float): Fitness value at generation t-1.
            f_t (float): Fitness value at generation t.

        Returns:
            Any: Output of the detection logic, defined by subclasses.
        """
        pass

    @abstractmethod
    def change_detection(self):
        """
        Abstract method to implement fitness change detection logic.
        Can include varying arguments
        """
        pass


# Example subclass implementation
class CustomChangeDetection(AbstractChangeDetection):
    """
    Custom implementation of the AbstractChangeDetection class.
    Uses the default logic for calculating Δf, a, and cd but customizes the detection logic.
    """

    def detect_change(self, f_t_minus_1, f_t, threshold=0.5):
        """
        Detects if a significant change occurred based on fitness values.

        Parameters:
            f_t_minus_1 (float): Fitness value at generation t-1.
            f_t (float): Fitness value at generation t.

        Returns:
            bool: True if change detection probability exceeds a threshold, otherwise False.
        """
        delta_f = self.calculate_fitness_change(f_t_minus_1, f_t)
        a = self.calculate_a(delta_f)
        cd = self.calculate_cd(a)
        # returns true if cd is greater than threshold otherwise false
        return cd > threshold
