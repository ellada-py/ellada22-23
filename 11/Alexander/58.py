a = int(input())
if a%400==0 or (a%100!=0 and a%4==0):
    print('Этот год високосный')
else:
    print('Этот год не високосный')
