s = 0
k = 0
while (True):
    a = int(input('Введите значение:'))
    if a != 0:
        s += a
        k += 1
    else:
        if k == 0:
            print ('Ошибка')
        else:
            print(s/k)
    break


