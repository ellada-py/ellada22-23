f=open('17.1.txt')
s=[int(k) for k in f]
count=0
max=0
for i in range(len(s)-1):
    for j in range (i+1,len(s)):
            pr=s[i]*s[j]
            if pr%26==0:
                count+=1
                if s[i]+s[j]>max:
                    max=s[i]+s[j]
print(count)
print(max)