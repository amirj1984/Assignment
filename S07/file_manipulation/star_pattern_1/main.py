# ****
# ****
# ****
# ****
fr = open("input.txt")
num = int(fr.readline())
pattern = fr.readline().strip()
fr.close()

line = num * pattern + "\n"
s = num * line

fw = open("output.txt", mode="w")
fw.write(s)
fw.close()
