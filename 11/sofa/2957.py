s= list(map(int,input().split()))
s[0]=s[-1]
for i in range(1,len(s),-1):
    s[i]=s[i-1]
print(s)