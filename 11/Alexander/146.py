from random import *
def qwe(a, b):
    list1 = []
    for i in range(5):
        f = randint(a, b)
        list1.append(f)
    return list1
d = dict.fromkeys(['B', 'I', 'N', 'G', 'O'],[])


d['B'] = qwe(1, 15)
d['I'] = qwe(16, 30)
d['N'] = qwe(31, 45)
d['G'] = qwe(46, 60)
d['O'] = qwe(61, 75)


for i in d.keys():
    print(i, end = '  ')
print(end = '\n')
for i in range(5):
    for j in d.keys():
        if len(str(d[j][i]))==1:
            print(d[j][i], end='  ')
        else:
            print(d[j][i], end = ' ')
    print(end = '\n')