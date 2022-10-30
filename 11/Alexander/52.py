a = input('Оченка: ')
bukv = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
qwe = [4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0]
if a in bukv:
    print(qwe[bukv.index(a)])
else:
    print('Неверный ввод')
