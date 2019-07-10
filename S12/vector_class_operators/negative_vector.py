# this program returns the negative vector of a given one using class vector.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Vector(-self.x, -self.y)


vec1 = Vector(3, 4)
vec2 = vec1.__neg__()
# vec2 = -vec1
print(vec2.x, vec2.y)

