# this code reads a positive integer number greater than 1 and indicates if it is a prime number or not (for loop and range)

num = int(input("enter a positive integer number greater than 1 : "))

is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False

print("is it a prime number", is_prime)
