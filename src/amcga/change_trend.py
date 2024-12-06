from abc import ABC, abstractmethod


class AbstractChangeTrend(ABC):
    """
    Abstract class for implementing the change trend scheme for both
    binary-encoded and real-valued problems.
    """

    def __init__(self, m_pv, pv):
        """
        Initialize the default parameters for change detection.

        Parameters:
            m_pv: holds the temporary probability vector (i.e. elite)
            pv: holds the current pv used for sampling solution
        """
        self.m_pv = m_pv
        self.pv = pv

    @abstractmethod
    def binary_encoded(self):
        """
        Abstract method for calculating the change trend for binary-encoded
        solutions based on the difference between m_pv and pv
        """
        pass

    @abstractmethod
    def real_valued(self):
        """
        Abstract method for calculating the change trend for real-valued
        solutions based on the difference between current elite solution and previous elite solution.
        This means that fitness value of both solutions are important
        """
        pass
