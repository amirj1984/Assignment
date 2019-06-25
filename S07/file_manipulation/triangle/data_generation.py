import random

fw = open('inp.txt', 'w')

for i in range(1000):
    for j in range(3):
        fw.write(str(random.randint(5, 20)))
        fw.write(' ')
    fw.write('\n')

fw.close()