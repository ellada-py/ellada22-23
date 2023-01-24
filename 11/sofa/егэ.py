d=[]
for i in range(35000000,40000001):
    for j in range(2, i):
        if i % j == 0:
            d.append(j)
    for l in range(len(d)):
        if int(d[l])%2:
            p=d.pop(l)
    print(d)