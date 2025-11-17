import random
import math
oszthato3 = 0
ketjegyu = random.randint(10,99)#20
osszes = 0
for i in range(ketjegyu):
    haromjegyu = random.randint(100,999)
    print(haromjegyu, end= " ")
    if haromjegyu %3 == 0:
        oszthato3 += 1
    osszes += haromjegyu
gyok = math.sqrt(osszes)
print()
print(oszthato3)
print(osszes)
print(round(gyok,2))