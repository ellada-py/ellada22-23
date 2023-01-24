f = open('27883 (1).txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
first = 543
second = 2358
del (data[0])
data = [int(i) for i in data]
data.sort()
for i in range(0, second):

print(data)