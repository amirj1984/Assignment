def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(num):
    while True:
        num = num + 1
        if is_prime(num):
            return num


for i in range(5, 100):
    print(i, next_prime(i))


#
# def next_prime(num):
#     next_num = num + 1
#     while True:
#         for i in range(2, next_num):
#             if next_num % i != 0:
#                 return next_num
#             else:
#                 next_num += 1
#
# print(next_prime(24))