from random import *
q = 0
for i in range(10):
    list2 = ''
    while 'ООО' not in list2 and 'РРР' not in list2:
        if randint(1,2) == 1:
            list2+='О'
        else:
            list2+='Р'
    print(list2, 'понадобилось %d попыток' % len(list2))
    q+=len(list2)
print('Среднее количество попыток: %s' % (q/10))
