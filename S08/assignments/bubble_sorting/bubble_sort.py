# this function resembles the bubble sorting

def bubble_sort(lst):
    """

    :param lst: list of numbers
    :return: sorted list from the lower to the higher values
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [6, 100, 4, 6, 55]
print(bubble_sort(lst))


