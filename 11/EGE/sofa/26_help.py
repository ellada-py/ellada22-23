
f = open('27883.txt')
data = f.readlines()
del (data[0])
a=643
b=2358
data=[int(i) for i in data]
print(data)