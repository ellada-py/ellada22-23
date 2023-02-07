f=open('17var02.txt')
s=[int(j) for j in f]
max=0
count=0
max2=0
for l in range (len(s)):
    if s[l]%2==0:
        if s[l]>max:
            max=s[l]
for i in range(len(s)-1):
    if s[i]+s[i+1]==max:
        count+=1
        if (s[i]**2)+(s[i+1]**2)>max2:
            max2=(s[i]**2)+(s[i+1]**2)
print(count)
print(max2)