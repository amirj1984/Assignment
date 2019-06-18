# this code reads a non-negative integer number and produces its factorial
num = input("enter a non-negative integer number whose factorial is desired: ")
num_int = int(num)
i = 1
fact = 1
if num == 0:
    print("1")
else:
    while i <= num_int:
        fact = fact * i
        i = i + 1
print(fact)

