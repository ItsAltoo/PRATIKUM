import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * (self.radius**2)
