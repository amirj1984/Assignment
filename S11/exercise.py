# raise Exception
# raise ZeroDivisionError
# raise Exception("your entered number is incorrect")

# Question: why only the value error is shown even by replacing the excepts nothing changed?
# from math import sqrt
#
# lst = [1, 2, 3]
# x = -6
#
#
# try:
#     square_root = sqrt(x)
#     print(square_root)
#     print(lst[3])
# except ValueError as e:
#     print(e.args)
#     print("the entry is invalid")
# except IndexError as e:
#     print(e.args)
#     print("index number is invalid")
# print("Bye!")

# string formatting

name = "Jack"
height = 177.1234
age = 35.973
# spec = name + "," + str(height) + "," + str(age)
# print(spec)
# spec = "{0}, {1}, {2}".format(name, height, age)
# print(spec)
# spec = "{name}, {age}, {name}, {height}, {name}".format(name=name, age=age, height=height)
# print(spec)
# spec = f"{name}, {age}, {name}, {height}, {name}"
# print(spec)
# print(f"({name},{height:.2f},{age:.2f})")
# print(f"({name:<15},{height:^+10.2f},{age:>+15.2f})")


