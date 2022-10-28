n=int(input('введите целое число (2 или больше): '))
factor=2
print('простые множители числа '+str(n)+':')
while factor<=n:
    if n%factor:
        factor+=1
    else:
        print(factor)
        n=n/factor