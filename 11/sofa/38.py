n=int(input('количество сторон фигуры (в диапозоне от 3 до 10): '))
if 3<=n<=10:
    print(str(n)+'-угольник')
else:
    print('количество сторон находится вне диапозона')