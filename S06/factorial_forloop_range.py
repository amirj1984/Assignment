# this code reads a positive integer number and gives its factorial
num = int(input("enter a positive integer number to produce its factorial: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)
