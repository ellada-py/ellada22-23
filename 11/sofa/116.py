n=int(input('введите число: '))
d=[]
sum=0
for i in range(1,n):
   if n%i==0:
       d.append(i)
       sum+=i
if sum==n:
    print('True')
else:
    print('False')