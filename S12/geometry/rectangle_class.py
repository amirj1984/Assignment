# this program returns area and perimeter of a rectangle using class rectangle and docstring test


class Rectangle:
    """
    EXAMPLE
    -------
    >>> rec = Rectangle(3, 5)
    >>> rec.area_of_rectangle()
    15.0
    >>> rec.perimeter_of_rectangle()
    16.0
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_of_rectangle(self):
        return self.length * self.width

    def perimeter_of_rectangle(self):
        return (self.length + self.width) * 2


rec = Rectangle(5, 3)
print("area of the rectangle is: ", rec.area_of_rectangle(), "\n", "perimeter of the rectangle is: ", rec.perimeter_of_rectangle())

if __name__ == "__main__":
    import doctest

    doctest.testmod()

