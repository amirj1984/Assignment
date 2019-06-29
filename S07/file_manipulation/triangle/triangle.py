# this program has an input file with 1000 triangles' sides. it indicates whether they can constitute a triangle and their type such as isosceles, right-angle, equilaterial or scalene
fr = open("inp.txt")
fw = open("output.txt", mode="w")

triangle_count = 0
triangle_isosceles = 0
tringle_equilateral = 0
triangle_right = 0

for i in range(1000):
    triangle_sides = fr.readline().split()
    for j in range(3):
        side_1 = int(triangle_sides[0])
        side_2 = int(triangle_sides[1])
        side_3 = int(triangle_sides[2])
        side_list = [side_1, side_2, side_3]
        side_list.sort(reverse=True)
    cond = side_1 + side_2 >= side_3 and side_2 + side_3 >= side_1 and side_1 + side_3 >= side_2
   
    if cond:
        triangle_count += 1 
        if side_1 == side_2 == side_3:
            triangle_isosceles += 1
        elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
            tringle_equilateral += 1
        if side_list[0] ** 2 == side_list[1] ** 2 + side_list[2] ** 2:
            triangle_right += 1
            
        # elif side_1 != side_2 and side_2 != side_3 and side_1 != side_3:



fw.write(str(triangle_count) + "\n")
fw.write("EQUILATERAL" + "\n")
fw.write("ISOSCELES" + str(triangle_isosceles) + "\n")
 

fw.close()
