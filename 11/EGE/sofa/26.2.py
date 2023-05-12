f=open('27881.txt') #задание: найти макимальное кол-во файлов ( и наиб из них) влезающих в данный обьем (а)
s=f.readlines()
del (s[0])
s=[int (i) for i in s]
s.sort()
d=4625
maxcount=0
max=0
for i in range (d-1):
    a=1987
    a-=s[i]
    count=1
    for j in range (i+1,d):
        if a>s[j]:
            a-=s[j]
            count+=1
            if count>maxcount:
                maxcount=count
                if s[j]>max:
                    max=s[j]
print(maxcount)
print(max)