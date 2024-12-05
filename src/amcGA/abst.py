from abc import ABC, abstractmethod
import random

class AbstractSolution(ABC):
    def __init__(self, value):
        self.value = value
        self.fitness = 0

    @abstractmethod
    def calculate_fitness(self, fitness_function):
        pass

class AbstractChangeDetection(ABC):
    def __init__(self, dfitness, mean=1, variance=0.3):
        self.dfitness = dfitness
        self.mean = mean
        self.variance = variance

    @abstractmethod
    def change_detection(self):
        pass

class AbstractAdaptiveMutation(ABC):
    def __init__(self, cd, m_pv, ml=0.01, mh=0.5, dl=0.0, dh=1.0):
        self.ml = ml
        self.mh = mh
        self.dl = dl
        self.dh = dh
        self.cd = cd
        self.m_pv = m_pv

    @abstractmethod
    def prob_mut(self):
        pm = self.ml + (self.cd - self.dl) * ((self.mh - self.ml) / (self.dh - self.dl))
        # Clip pm to the range [0.01, 0.5]
        return max(0.01, min(pm, 0.5))
    
    @abstractmethod
    def am1(self, pm):
        r = random.random()
        for p in self.m_pv:
            self.m_pv[p] = random.uniform(self.cd, self.m_pv[p]) if r < pm else self.m_pv[p]

    @abstractmethod
    def am2(self, pm):
        r = random.random()
        for p in self.m_pv:
            self.m_pv[p] = abs(self.m_pv[p] + (r - pm)) if r < pm else self.m_pv[p]

    @abstractmethod
    def am3(self, pm):
        r = random.random()
        adjustment = (r - pm) / 2 
        for p in self.m_pv:
            self.m_pv[p] = self.m_pv[p] + adjustment if r < pm else self.m_pv[p] - adjustment

