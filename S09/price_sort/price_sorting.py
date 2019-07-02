from price_input import btc

print(btc)

# f = lambda x: x[2] - x[1]
# g = sorted(btc, reverse=True, key=f)
# print(g)

# f2 = lambda x: x[2] - x[1]
# g2 = max(btc, key=f2)
# print(g2)

# f3 = lambda x: x[-1]
# g3 = max(btc, key=f3)
# print(g3)

# f4 = lambda x: x[-1]
# g4 = sorted(btc, key=f4, reverse=True)
# print(g4)

# n = [0, 1, 2, 3, 4]
# # print([2 * k + 1 for k in n])
# f = lambda x: 2 * x + 1
# out = map(f, n)
# for d in out:
#     print(d)



# f = lambda x: x[2] - x[1]
# g = [f(k) for k in btc]
# print(g)

# f = lambda x: x[2] - x[1]
# out = map(f, btc)
# for d in out:
#     print(d)
# print(list(out))

f = lambda x: x[-1] > 700
# out = list(map(f, btc))
# print(out)

# out = list(filter(f, btc))
# print(out)

out = [j for j in btc if f(j)]
print(out)