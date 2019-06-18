# this code reads a positive integer number and accumulates the sum of inverse numbers power 2. if it goes to infinit, it equals to pi^2/6.
num = input("enter a positive integer number to calculate Riemann zeta function: ")
num_int = int(num)
i = 1
sum_of_numbers = 0

while i <= num_int:
    sum_of_numbers = sum_of_numbers + 1/i ** 2
    i = i + 1

print((sum_of_numbers*6) ** 0.5)

