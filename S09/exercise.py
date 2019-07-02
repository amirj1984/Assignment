# def fun(x, y):
#     return x ** 2 + y ** 2
#
# print(fun(2, 3))


# f = lambda x, y: (x ** 2 + y ** 2)
# print(f(10, 1))

# lst = [-9, -2, 0, 1, 2, 7]
             # print(lst.sort()) => none
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# f = sorted(lst)
# print(f)

# f = sorted(lst, key=abs)
# print(f)

# f = lambda x: abs(2 - x)
# lst = [0, 1, 5]    #f(0)= 2, f(1) = 1, f(5) = 3
# g = sorted(lst, key=f)
# print(g)

# lst = [(1, 10), (1, 4), (3, -3), (45, 1), (90, -1)]
# # g = sorted(lst)
# # print(g)
# f = lambda x: abs(x[1] - x[0])
# dif = sorted(lst, key=f)
# print(dif)

lst = [(0, 1), (1, 0), (2, -1), (-1, 2)]
f = lambda x: x[1] - x[0]
g = sorted(lst, key=f)
print(g)




