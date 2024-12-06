"""
import key modules
"""

from abc import ABC, abstractmethod
import random


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
