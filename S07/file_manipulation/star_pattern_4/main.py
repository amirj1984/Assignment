#    *
#   * *
#  *****
# *     *
fr = open("input.txt")
num = int(fr.readline())
i = int(fr.readline())
pattern = fr.readline().strip()
fr.close()

line = ""
while i <= num:
    white = " " * (num - i)
    if i % 2 == 1:
        stars = pattern * (2 * i - 1)
    else:
        mid_white = " " * (2 * i - 3)
        stars = pattern + mid_white + pattern
    line = line + white + stars + white + "\n"
    i = i + 1

fw = open("output.txt", mode="w")
fw.write(line)
fw.close()

