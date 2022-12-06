f=open('24.txt')
s=f.read()
max1=1
max2=0
for i in range (len(s)-1):
    if s[i]!='P':
        max2+=1
    elif s[i]=='P' and s[i+1]!='P':
        max2+=1
    else:
        if max2>max1:
            max1=max2
            max2=0
print(max1)