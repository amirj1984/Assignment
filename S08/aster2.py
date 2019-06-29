def my_sum(*numbers):
    s = 0
    for num in numbers:
        s = s + num
    return s

val = my_sum(2, 43, 65, 1000)
print(val)