from random import *
def kto_pobedil():
    f = randint(0,37)
    if f == 37:
        print('Выпал номер: 00')
        print('Выиграла ставка: 00')
    elif f == 0:
        print('Выпал номер: 0')
        print('Выиграла ставка: 0')
    else:
        print('Выпал номер:', f)
        print('Выиграла ставка', f)
        f = randint(1, 2)
        if f == 1:
            print('Выиграла ставка: чёрное')
        else:
            print('Выиграла ставка: белое')
        f = randint(1, 2)
        if f == 1:
            print('Выиграла ставка: чётное')
        else:
            print('Выиграла ставка: нечётное')
        f = randint(1, 2)
        if f == 1:
            print('Выиграла ставка: от 1 до 18')
        else:
            print('Выиграла ставка: от 19 до 36')

kto_pobedil()