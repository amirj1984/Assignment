# this program calculates subtraction of vectors using class od vectors


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x_new = self.x - other.x
        y_new = self.y - other.y
        return Vector(x_new, y_new)


vec1 = Vector(3, 5)
vec2 = Vector(7, 7)
vec3 = vec1 - vec2
print(vec3.x, vec3.y)

