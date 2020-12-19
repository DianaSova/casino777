import random
from cube import dice

class chitcube(dice):
    value = 3
    def roll(self):
        return round(random.triangular(1,6,self.value))

class mathcube(dice):
    multiplier = 10
    def roll(self):
        return super().roll() * self.multiplier