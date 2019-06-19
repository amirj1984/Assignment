# this code reads a list and indicates whether it is a symmetrical one or not.
lst = eval(input("Write a list"))
i = 0
length_lst = len(lst)
is_sym_lst = True

while i < length_lst/2:
    if lst[i] != lst[length_lst - i - 1]:
        is_sym_lst = False
        break
    i = i + 1

print("is it a symmetrical list? ", is_sym_lst)


