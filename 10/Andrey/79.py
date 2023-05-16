a = int(input('Введите первое число: - '))
b = int(input('Введите второе число: - '))
if a < b:
    d = a
else:
    d = b
while a % d != 0 or b % d !=0:
    d = d - 1
print(d)