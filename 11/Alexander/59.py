a = input().split()
god = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля','августа','сентебря','октября','ноября','декабря']
a31 = ['июля', 'августа', 'октября', 'декабря', 'января', 'марта', 'мая']
a30 = ['июня', 'сентября', 'ноября', 'апреля']
if a[1] in a31 and int(a[0])>31:
    print('Ошибка')
elif a[1] in a30 and int(a[0])>30:
    print('Ошибка')
elif a[1]=='декабря' and a[0]=='31':
    print('1 января', int(a[2])+1)
elif (int(a[2])%400==0 or (int(a[2])%100!=0 and int(a[2])%4==0)):
    if a[1]=='февраля' and a[0]=='28':
        print('29 февраля', a[2])
elif a[1] == 'февраля' and int(a[0])>28 and ((int(a[2])%400==0 or (int(a[2])%100!=0 and int(a[2])%4==0))==False):
    print('Ошибка')
elif a[1] in a31 and a[0]=='31':
    print('1', god[god.index(a[1])+1], a[2])
elif a[1] in a30 and a[0]=='30':
    print('1', god[god.index(a[1])+1], a[2])
elif a[1]=='февраля' and a[0]=='28':
    print('1', god[god.index(a[1])+1], a[2])
elif a[1] in god:
    print(int(a[0])+1, a[1], a[2])
else:
    print("Ошибка")