# this program returns area & perimeter of a square using class square and docstring test


class Square:
    """
    EXAMPLE
    -------
    >>> sq = Square(3.0)
    >>> sq.area_of_square()
    9.0
    >>> sq.perimeter_of_square()
    12.0
    """
    def __init__(self, side: float):
        self.side = side

    def area_of_square(self) -> float:
        return self.side ** 2

    def perimeter_of_square(self) -> float:
        return self.side * 4


sq = Square(2.5)
print("area of the square is: ", sq.area_of_square(), "\n", "perimeter of the square is: ", sq.perimeter_of_square())

if __name__ == "__main__":
    import doctest

    doctest.testmod()
