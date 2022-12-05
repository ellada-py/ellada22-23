from random import *

list1 = []
while len(list1)!=6:
    f = randint(1,49)
    if f not in list1:
        list1.append(f)
print(*list1)