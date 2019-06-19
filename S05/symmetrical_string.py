# this code reads a string and indicates whether it is a symmetrical one or not.
str_raw = input("Write a string: ")
i = 0
length_str = len(str_raw)
is_sym_str = True

while i < length_str/2:
    if str_raw[i] != str_raw[length_str - i - 1]:
        is_sym_str = False
        break
    i = i + 1

print("is it a symmetrical string? ", is_sym_str)
