# original.py
import numpy as np
from numpy.linalg import solve
from numpy.random import RandomState


class OriginalSimulation:
    def __init__(self):
        self.rng = RandomState(42)  # Same seed as optimized version

    def simulate(self, n):
        A = self.rng.rand(n, n)
        B = self.rng.rand(n, n)
        C = self.rng.rand(n, n)
        D = np.dot(A, B)
        E = D * C
        return solve(E, np.ones(n))
