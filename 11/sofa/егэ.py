d=[]
for i in range (35000000,40000001):
    for j in range(1,i+1):
        if i%j:
            d.append(j)
    for l in range (len(d)):
        if d[l]%2:
            p=d.pop(l)
    if len(d)==5:
        print(i)