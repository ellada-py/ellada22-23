n=int(input('введите число: '))
p=2
numbers=[]
for i in range(n+1):
    numbers.append(int(i))
numbers[1]=0
while p<n:
    for i in range(p+1,n+1):
        if numbers[i]%p==0:
            numbers[i]=0
    p+=1
k=[]
for i in range(len(numbers)):
    if numbers[i]!=0:
        k.append(numbers[i])
print(k)