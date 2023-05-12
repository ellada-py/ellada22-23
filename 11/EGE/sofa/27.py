f=open('28129_A.txt')
s=[int(i) for i in f]
d=160
p=7
max=0
for i in range(1,s[0]):
    if (s[i]%d!=s[i+1]%d) and ((s[i]%p==0) or (s[i+1]%p==0)):
        if s[i]+s[i+1]>max:
            max=s[i]+s[i+1]
            para=[s[i],s[i+1]]
print(para)
