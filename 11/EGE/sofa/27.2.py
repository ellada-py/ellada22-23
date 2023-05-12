f=open('28129_B.txt')
s=[int(i) for i in f]
d=160
p=7
max=0
for i in range(1,s[0]):
    for j in range(i+1,s[0]+1):
        if (s[i]%d!=s[j]%d) and ((s[i]%p==0) or (s[j]%p==0)):
            if s[i]+s[j]> max:
                max=s[i]+s[j]
                para=[s[i],s[j]]
print(para)