numbers=input('введите числа через пробел: ').split(' ')
if (numbers == sorted(numbers)) or (numbers== sorted(numbers, reverse=True)):
    print(True)
else:
    print(False)