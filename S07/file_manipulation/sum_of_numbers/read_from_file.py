fread = open("input.txt")
numbers = fread.read().split("\n")
fread.close()

sum_of_numbers = 0
for n in numbers:
    sum_of_numbers = sum_of_numbers + int(n)

fw = open("output.txt", mode="w")
fw.write(str(sum_of_numbers))
fw.close()







