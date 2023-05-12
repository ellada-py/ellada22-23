s=list(map(int,input().split()))
for i in range(len(s)-1,-1,-1):
    s[i]=s[i-1]
print(s)