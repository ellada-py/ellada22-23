f=open('17.txt')
a=[int(i) for i in f]
sum=0
k=0
for i in range(len(a)):
    if a[i]%2:
        sum+=a[i]
        k+=1
sr=sum/k
count=0
max=0
for j in range(len(a)-1):
    if ((a[j]%3==0) or (a[j+1]%3==0)) and ((a[j]<sr) or (a[j+1]<sr)):
        count+=1
        if a[j]+a[j+1]>max:
            max=a[j]+a[j+1]
print(count)
print(max)