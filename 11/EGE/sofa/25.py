count=0
maxcount=0
max=0
for i in range (79201,80000):
    count=0
    s=i
    for j in range(1,int(s**0.5)+1):
        if i%j==0:
            count+=1
            i=i//j
            if count>maxcount:
                maxcount=count
                max=s
print(maxcount)
print(max)


mk=0
mi=0
for i in range(568023, 569231):
    k=2
    d=2
    while d * d < i:
        if i%d==0:
            k+=2
        d+=1
    if d*d==i:
        k+=1
    if k>mk:
        mk=k
        mi=i
print(mk, mi)


i=568260
s=0
for j in range(1, int(i ** 0.5)):
    if i % j == 0:
        s+= 1
        i = i // j
        print(j, end='  ')
print(s)

