numbers=input('введите числа через пробел: ').split(' ')
min=float(input('минимальный порог: '))
max=float(input('максимальный порог: '))
CountRange=0
for i in range(len(numbers)):
    numbers[i]=float(numbers[i])
for i in range(len(numbers)):
    if min<=numbers[i]<max:
        CountRange+=1
print(CountRange)