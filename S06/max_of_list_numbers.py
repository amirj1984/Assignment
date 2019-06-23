# this code reads a list of numbers and returns its maximum member
lst = eval(input("enter a list of numbers: "))

mx = lst[0]

for num in lst:
    if num > mx:
        mx = num
print(mx)
