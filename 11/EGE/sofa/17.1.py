f=open('17 (4).txt')
s=[int(k) for k in f]
max=0
count=0
for i in range (len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]*s[j]%10==0:
            count+=1
            if s[i]+s[j]>max:
                max=s[i]+s[j]
print(count)
print(max)