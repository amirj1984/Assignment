# this program reads an input file including sides of triangles and returns if they can constitute a triangle and of which type
# it provides numbers of triangles, and each type


def extract_data(raw_data):
    """

    :param raw_data: 1000 rows of three numbers
    :return: it splits each row
    """
    lines = raw_data.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines


fname = "./../../../S07/file_manipulation/triangle/inp.txt"

data = (open(fname).read())
triangles = (extract_data(data))


def is_triangle(sides):
    """

    :param sides: three sides of hypothetical triangles
    :return: False: if these sides don't constitute a triangle.
            True: if the sides constitute a triangle
    """
    if len(sides) != 3:
        return False
    else:
        a, b, c = sides
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False


def triangle_type(triangle):
    """

    :param triangle: sides of triangles
    :return: their type including equilateral, isosceles and/or right-angled
    """
    types = []
    tri_sorted = sorted(triangle)
    if is_triangle(triangle):
        if triangle[0] == triangle[1] == triangle[2]:
            types.insert(0, "equi")
        if triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]:
            types.insert(1, "isos")
        if tri_sorted[0] ** 2 + tri_sorted[1] ** 2 == tri_sorted[2] ** 2:
            types.insert(2, "right-angled")
        return types


count_triangle = 0

for triangle in triangles:
    print(triangle)
    if is_triangle(triangle):
        count_triangle += 1
        print("triangle", triangle_type(triangle))

print("number of triangles: ", count_triangle)



def is_isosceles(sides):
    """

    :param sides: sides of triangles
    :return: if a triangle is isosceles
    """
    a, b, c = sides
    if is_triangle(triangle):
        if a == b or b == c or a == c:
            return True
        return False


def is_equilateral(sides):
    """

    :param sides: sides of triangles
    :return: if a triangle is equilateral
    """
    a, b, c = sides
    if is_triangle(triangle):
        if a == b and b == c and a == c:
            return True
        return False


def is_right_angled(sides):
    """

    :param sides: sides of triangles
    :return: if a triangle is right-angled
    """
    sides_sort = sorted(sides)
    if is_triangle(triangle):
        if sides_sort[0] ** 2 + sides_sort[1] ** 2 == sides_sort[2] ** 2:
            return True
        return False


count_equilateral = count_isosceles = count_triangle = count_right_angled = 0

for triangle in triangles:
    if is_triangle(triangle):
        count_triangle += 1
    if is_isosceles(triangle):
        count_isosceles += 1
    if is_equilateral(triangle):
        count_equilateral += 1
    if is_right_angled(triangle):
        count_right_angled += 1

print("number of isosceles triangles: ", count_isosceles, "number of equilateral triangles: ", count_equilateral, "number of right-angled triangles: ", count_right_angled, sep="\n")

