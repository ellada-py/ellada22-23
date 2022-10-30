def dis(a, b, c):
    d = b**2-(4*a*c)
    if d<0:
        print('решений нет')
    elif d==0:
        print(1, end = ' ')
        zna(a, b, d, 0)
    else:
        print(2, end = ' ')
        zna(a, b, d, 0)
        zna(a, b, d, 1)
def zna(a, b, d, c):
    if c==0:
        print((-b+d**0.5)/(2*a), end = ' ')
    else:
        print((-b - (d ** 0.5)) / (2 * a), end=' ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
dis(a, b, c)
