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


# class Tree:
#     is_something = True
#     name = "derakht"
#
#     def get_height_of_tree(tree):
#         return tree.height
#
#
# tree_1 = Tree()
# tree_1.name = "chenar"
# tree_1.height = 12
#
# tree_2 = Tree()
# tree_2.name = "sarv"
# tree_2.height = 10
#
# tree_3 = Tree()
# tree_3.age = 55
# tree_3.height = 14

# for tree in [tree_1, tree_2, tree_3]:
#     # print(tree.name, tree.is_something, tree.height)
#     print(tree.__dict__)
# print(Tree.__dict__)

# res = get_height_of_tree(tree_1)
# print(res)

# res = Tree.get_height_of_tree(tree_1)
# print(res)

# print(tree_1.get_height_of_tree())

class Tree:
    def __init__(self, a, c, h):
        self.age = a
        self.color = c
        self.height = h


tree_1 = Tree(77, "green", 12)
tree_2 = Tree(90, "Brown", 21)

for tree in [tree_1, tree_2]:
    print(tree.__dict__)
