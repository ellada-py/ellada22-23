count=0 #ответ: 612
n=0
def f(x):
    count=0
    if x[0]=="4":
        if int(x[1])%2==0:
            count+=1
    elif x[-1]=='4':
        if int(x[-2])%2==0:
            count+=1
    else:
        for i in range (1,len(x)-1):
            if x[i]=='4':
                if (int(x[i-1])%2==0) and (int(x[i+1])%2==0):
                    count+=1
    if count==2:
        return 1
    else:
        return 0
for i in range (10000,100000):
    count2 = 0
    x=str(oct(i))
    for j in range(len(x)):
        if x[j]=='4':
            count2+=1
            if count2>2:
                break
    if count2==2:
        s =x[2:]
        count+=f(s)

print(count)