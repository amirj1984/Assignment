# this program takes a vector and returns its length using class vector

from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)


vec1 = Vector(2, 4)
print(vec1.vector_length())

