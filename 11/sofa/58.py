year=int(input('год: '))
if year%400==0:
    print('это високосный год')
elif year%100==0:
    print('это не високосный год')
elif year%4==0:
    print('это високосный год')
else:
    print('это не високосный год')