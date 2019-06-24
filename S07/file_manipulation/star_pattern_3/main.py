#    *
#   * *
#  *   *
# *******
fr = open("input.txt")
num = int(fr.readline())
mid_white = int(fr.readline())
pattern = fr.readline().strip()
fr.close()

line_1 = (num - 1) * " " + pattern + "\n"

s = ""
while mid_white < num:
    line = (num - mid_white) * " " + pattern + (2 * mid_white - 3) * " " + pattern
    s = s + line + "\n"
    mid_white = mid_white + 1

line_end = (2 * num - 1) * pattern

fw = open("output.txt", mode="w")
fw.write(line_1)
fw.write(s)
fw.write(line_end)
fw.close()