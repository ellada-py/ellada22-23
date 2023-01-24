count=0
n=0
for i in range (10000,100000):
    count2 = 0
    x=str(oct(i))
    for j in range(len(x)):
        if x[j]=='4':
            count2+=1
            if count2>2:
                break
    if count2==2:
        for k in range(1, len(x) - 1):
            s = int(x[2:])
            if x[k] == 4:
                if (x[k - 1] % 2 == 1) or (x[k + 1] % 2 == 1):
                    n=0
                else:
                    n=1
    count= count +n
print(oct(10004))
print(count)