for i in range (35000000,40000001):
    d=[]
    for j in range(1,i+1):
        if (j%2==1) and(i%j==0):
            d.append(j)
    if len(d)==5:
        print(i)