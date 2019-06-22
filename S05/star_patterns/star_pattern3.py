#      *
#     * *
#    *****
#   *     *
#  *********
# *         *

white_space = " "
txt = "*"
white_space_num = 5
txt_num = 0
i = 1

while txt_num <= 5 and white_space_num >= 0 and i <= 6:
    if i % 2 == 1:
        print(white_space_num * white_space + (2 * txt_num + 1) * txt)
    else:
        print(white_space_num * white_space + txt + (2 * i - 3) * white_space + txt)

    white_space_num = white_space_num - 1
    txt_num = txt_num + 1
    i = i + 1