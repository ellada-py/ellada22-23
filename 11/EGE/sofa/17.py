f=open('17.txt')
s=[int(j) for j in f]
sum=0
k=0
for l in range (len(s)):
    if s[l]%2==0:
        sum+=s[l]
        k+=1
a=sum/k
count=0
max=0
for i in range(len(s)-1):
    if (((s[i]%5==0) or (s[i+1]%5==0)) and ((s[i]<a) or (s[i+1]<a))):
        count+=1
        if s[i]+s[i+1]>max:
            max=s[i]+s[i+1]
print(count)
print(max)