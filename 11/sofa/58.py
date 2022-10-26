year=int(input('год: '))
if (year%400==0) or ((year%4==0) and (year%100!=0)):
    print('это високосный год')
else:
    print('это не високосный год')