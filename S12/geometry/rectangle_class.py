# this program returns area and perimeter of a rectangle using class rectangle


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_of_rectangle(self):
        return self.length * self.width

    def perimeter_of_rectangle(self):
        return (self.length + self.width) * 2


rec = Rectangle(5, 3)
print("area of the rectangle is: ", rec.area_of_rectangle(), "\n", "perimeter of the rectangle is: ", rec.perimeter_of_rectangle())

