# this program returns area and perimeter of a square using class square


class Square:
    def __init__(self, side):
        self.side = side

    def area_of_square(self):
        return self.side ** 2

    def perimeter_of_square(self):
        return self.side * 4


sq = Square(5)
print("area of the square is: ", sq.area_of_square(), "\n", "perimeter of the square is: ", sq.perimeter_of_square())

