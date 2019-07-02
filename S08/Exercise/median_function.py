 
def median(*numbers):
    n = len(numbers)
    if n % 2 == 1:
        return sorted(numbers)[n//2]
    elif n % 2 == 0:
        return (sorted(numbers)[int(n/2 - 1)] + sorted(numbers)[int(n/2)])/2

print(median(1))
