#      *
#     ***
#    *****
#   *******
#  *********
# ***********

white_space = " "
txt = "*"
white_space_num = 5
txt_num = 0
while txt_num <= 5 and white_space_num >= 0:
    print(white_space_num * white_space + (2 * txt_num + 1) * txt)
    white_space_num = white_space_num - 1
    txt_num = txt_num + 1


