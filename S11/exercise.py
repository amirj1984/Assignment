# raise Exception
# raise ZeroDivisionError
# raise Exception("your entered number is incorrect")

# Question: why only the value error is shown even by replacing the excepts nothing changed?
from math import sqrt

lst = [1, 2, 3]
x = -6


try:
    square_root = sqrt(x)
    print(square_root)
    print(lst[3])
except ValueError as e:
    print(e.args)
    print("the entry is invalid")
except IndexError as e:
    print(e.args)
    print("index number is invalid")
print("Bye!")