a = input('Введите букву: ')
b = int(input('Введите цифру: '))
if a == 'a' or a == 'c' or a == 'e' or a == 'g':
    if b % 2 == 0:
        print('Белая')
    else:
        print('Черная')
else:
    if b % 2 == 0:
        print('Черная')
    else:
        print('Белая')