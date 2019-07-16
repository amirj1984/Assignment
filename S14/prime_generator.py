import math

def is_prime(n: int):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0 :
            return False
    return  True


def prime_gen():
    yield 2
    i = 3
    while True:
        # yield i

        if is_prime(i):
            yield i
        i += 2


gen = prime_gen()
for i in gen:
    print(i)


    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False
    #     return True
    #
    #
    #
    # while True:
    #



