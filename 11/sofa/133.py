larger=input('введите числа через пробел: ').split(' ')
smaller=input('введите числа через пробел: ').split(' ')
n=larger.index(smaller[0])
k=0
for i in range(len(smaller)):
    if smaller[i]==larger[n+i]:
        k+=1
if k==len(smaller):
    print(True)
else:
    print(False)