from random import *

def qwe(a, b):
    list1 = []
    for i in range(5):
        f = randint(a, b)
        list1.append(f)
    return list1

def sozdanie():
    d = {}
    d['B'] = qwe(1, 15)
    d['I'] = qwe(16, 30)
    d['N'] = qwe(31, 45)
    d['G'] = qwe(46, 60)
    d['O'] = qwe(61, 75)
    return d

def pechat_kartochka(d):
    for i in d.keys():
        print(i, end='  ')
    print(end='\n')
    for i in range(5):
        for j in d.keys():
            if len(str(d[j][i])) == 1:
                print(d[j][i], end='  ')
            else:
                print(d[j][i], end=' ')
        print(end='\n')

def dostaem_i_zacrkivaem(d):
    z = [i for i in range(1,76)]
    shuffle(z)
    while proverka1(d):
        shuffle(z)
        f = z[0]
        z.pop(0)
        print(f, end = ' ')
        for j in d.keys():
            while f in d[j]:
                d[j][d[j].index(f)] = 0

def proverka1(d):
    list1 = []
    qwe = 0
    qwe1 = 0
    for i in d.keys():
        list1.append(d[i])
    for i in range(5):
        if sum(list1[i]) == 0:
            print('\n\nПобеда по вертикали')
            return False
        c = 0
        for j in range(5):
            c += list1[j][i]
            if i==j:
                qwe+=list1[i][j]
            if i+j==4:
                qwe1+=list1[i][j]
        if c == 0:
            print('\n\nПобеда по горизонатали')
            return False
    if qwe == 0:
        print('\n\nПобеда по диагонали')
        return False
    if qwe1 == 0:
        print('\n\nПобеда по вторичной диагонали')
        return False
    return True

def povtor():
    a = input('\nХотите сыграть снова?(Y/N) ')
    if a == 'Y':
        print()
        igra()
    else:
        print('До свидания')

def igra():
    d = sozdanie()
    pechat_kartochka(d)
    print()
    dostaem_i_zacrkivaem(d)
    print()
    pechat_kartochka(d)
    povtor()

igra()
