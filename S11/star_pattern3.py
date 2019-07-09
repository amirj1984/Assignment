for i in  range(7):
    pat = "*" * i
    if i % 2 == 0:
        print(f"{pat:<6}")
    else:
        print(f"{pat:>6}")


#      *
# **
#    ***
# ****
#  *****
# ******