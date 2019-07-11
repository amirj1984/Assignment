# this program calculates area and perimeter of parallelograms, diamonds (rhombus), rectangles and squares
# using class inheritance

from math import sin, radians


class Parallelogram:
    """
    EXAMPLE 1(parallelogram)
    ---------
    >>> par = Parallelogram(15.8, 24.6, 123)
    >>> par.area()
    325.97

    EXAMPLE 2 (diamond or rhombus)
    >>> diam = Diamond(2.0, 33)
    >>> diam.area()
    2.18

    EXAMPLE 3 (rectangle)
    -------
    >>> rec = Rectangle(3.0, 10.0)
    >>> rec.area()
    30.0

    EXAMPLE 4 (square)
    >>> sq = Square(5.25)
    >>> sq.area()
    27.56

    """
    def __init__(self, side1: float, side2: float, theta: float):
        self.side1 = side1
        self.side2 = side2
        self.theta = theta

    def area(self) ->float:
        return round(self.side1 * self.side2 * sin(radians(self.theta)), 2)

    def perimeter(self) ->float:
        return round(((self.side1 + self.side2) * 2), 2)


class Diamond(Parallelogram):
    def __init__(self, side: float, theta: float):
        super().__init__(side, side, theta)


class Rectangle(Parallelogram):
    def __init__(self, length: float, width: float):
        super().__init__(length, width, theta=90)


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


class Square2(Diamond):
    def __init__(self, side: float):
        super().__init__(side, theta=90)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# par = Parallelogram(6, 8, 60)
# print(par.area(), par.perimeter())
#
# diam = Diamond(2, 33)
# print(diam.area(), diam.perimeter())
#
# rec = Rectangle(4, 3)
# print(rec.area(), rec.perimeter())
#
# sq = Square(8)
# print(sq.area(), sq.perimeter())
#
# sq2 = Square2(8)
# print(sq2.area(), sq2.perimeter())

