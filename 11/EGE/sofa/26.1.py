f = open('27883.txt')
data = f.readlines()
del (data[0])
b=2358
data=[int(i) for i in data]
data.sort()
print(data)
max=data[0]
maxcount=0
for i in range (0,b):
    a=643
    a-=data[i]
    count=1
    for j in range(i+1,b):
        if a>data[j]:
            a-=data[j]
            count+=1
            if count>maxcount:
                maxcount=count




