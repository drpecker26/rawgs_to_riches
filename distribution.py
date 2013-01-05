import random

class UniformDistribution:
    """a uniform random distribution"""

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __call__(self):
        return random.uniform(self.min_val, self.max_val)
