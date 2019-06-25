# this program has an input file with 1000 triangles' sides. it indicates whether they can constitute a triangle and their type such as isosceles, right-angle, equilaterial or scalene
fr = open("inp.txt")
fw = open("output.txt", mode="w")
for i in range(1000):
    triangle_sides = fr.readline().split()
    fw.write(str(triangle_sides) + "\n")
    for j in range(3):
        side_1 = int(triangle_sides[0])
        side_2 = int(triangle_sides[1])
        side_3 = int(triangle_sides[2])
        side_list = [side_1, side_2, side_3]
        side_list.sort(reverse=True)
    cond = side_1 + side_2 >= side_3 and side_2 + side_3 >= side_1 and side_1 + side_3 >= side_2
    if cond:
        fw.write("Triangle" + "\n")
    else:
        fw.write("NOT Triangle" + "\n")

    if cond and side_1 == side_2 == side_3:
        fw.write("EQUILATERAL" + "\n")
    elif cond and side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        fw.write("ISOSCELES" + "\n")
    elif cond and side_list[0] ** 2 == side_list[1] ** 2 + side_list[2] ** 2:
        fw.write("RIGHT-ANGLED" + "\n")
    elif cond and side_1 != side_2 and side_2 != side_3 and side_1 != side_3:
        fw.write("SCALENE" + "\n")
