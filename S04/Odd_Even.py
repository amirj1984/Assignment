# this code reads a number and says if it is even or odd

num_raw = input("enter your chosen integer number: ")
num = int(num_raw)

if num % 2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")
