# a function that returns the hypotenuse of a right-angled triangle by taking other two sides' length


def hypotenuse(a, b):
    from math import sqrt
    c = sqrt(a ** 2 + b ** 2)
    return c


print(hypotenuse(6, 8))








