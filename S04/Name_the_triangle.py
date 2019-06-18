# This code reads three suggested sides' lengths of a triangle. Firstly, it distinguishes if they can constitute a triangle. then, it says its type (equilateral, isosceles, right-angled or scalene)
side_1 = input("enter the first side's length of the triangle: ")
side_2 = input("enter the second side's length of the triangle: ")
side_3 = input("enter the third side's length of the triangle: ")
side_1_float = float(side_1)
side_2_float = float(side_2)
side_3_float = float(side_3)
side_list = [side_1_float, side_2_float, side_3_float]
side_list.sort(reverse=True)

cond = side_1_float + side_2_float >= side_3_float and side_2_float + side_3_float >= side_1_float and side_1_float + side_3_float >= side_2_float

if cond:
    print("these sides' lengths can constitute a triangle")
else:
    print("these sides' lengths cannot constitute a triangle")

if cond and side_1_float == side_2_float == side_3_float:
    print("these sides' lengths represents an equilateral triangle")
elif cond and side_1_float == side_2_float or side_1_float == side_3_float or side_2_float == side_3_float:\
    print("these sides' lengths represents an isosceles triangle")
elif cond and side_list[0]**2 == side_list[1]**2 + side_list[2]**2:
    print("these sides' lengths represents a right-angled triangle")
elif cond and side_1_float != side_2_float and side_2_float != side_3_float and side_1_float != side_3_float:
    print("these sides' lengths represents a scalene triangle")









