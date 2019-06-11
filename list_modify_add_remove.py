motorcycles = ["Honda", "Ducati", "Kawasaki"]
print(motorcycles)
motorcycles[1] = "BMW"
print(motorcycles)
motorcycles.append("Ducati")
print(motorcycles)
motorcycles.insert(1, "Suzuki")
print(motorcycles)
del motorcycles [1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
popped_motorcycle_2 = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle_2 + " is the motorcycle that I like most.")
motorcycles.remove("Honda")
print(motorcycles)

