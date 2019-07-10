# Question: Why line 18 does not result in a correct answer???
# this program adds two vectors and represents it

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, another):
        x_new = self.x + another.x
        y_new = self.y + another.y
        return Vector(x_new, y_new)

    def __repr__(self):
        return f"VECTOR {self.x}, {self.y}"


vec1 = Vector(3, 5)
vec2 = Vector(11, 12)
vec3 = vec1+vec2
# print(Vector.add_vectors(vec1, vec2))
print(repr(vec3))


