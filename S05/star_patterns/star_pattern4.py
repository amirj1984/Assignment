#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********
white_space = " "
txt = "*"
white_space_num = 5
print(white_space_num * white_space + txt)

i = 0

while white_space_num >= 1 and i <= 3:
        print((white_space_num - 1) * white_space + txt + (2 * i + 1) * white_space + txt)
        white_space_num = white_space_num - 1
        i = i + 1

white_space_num = 5
print((2 * white_space_num + 1) * txt)

