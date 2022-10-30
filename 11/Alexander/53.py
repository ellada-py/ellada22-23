a = float(input('Оченка: '))
bukv = ['F', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
qwe = [0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.1]
if a>0:
    for i in range(len(qwe)-1):
        if qwe[i] < a <= qwe[i+1]:
            print(bukv[i+1])
            break
    else:
        print('A+')
elif a==0:
    print('F')
else:
    print('Неверный ввод')