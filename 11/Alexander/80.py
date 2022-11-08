n = int(input('Введите число(2 или больше): '))
q = n
list1 = []
factor = 2
while factor <= n:
    if n%factor==0:
        list1.append(factor)
        n//=factor
    else:
        factor+=1
print("Простые множители числа %d:" % q)
print(*list1)
