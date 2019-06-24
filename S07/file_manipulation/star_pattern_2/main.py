#    *
#   ***
#  *****
# *******
fr = open("input.txt")
num = int(fr.readline())
num_center = int(fr.readline())
pattern = fr.readline().strip()
fr.close()


s = ""
for i in range(num):
    line = (2 * i + 1) * pattern
    s = s + line.center(2 * num_center - 1) + "\n"

fw = open("output.txt", mode="w")
fw.write(s)
fw.close()