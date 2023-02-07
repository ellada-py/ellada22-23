delit = 123
for j in range(4):
    x = int('32'+'0'*j+'823')
    if x % delit == 0:
        print(x, end='   ')
        print(x//delit)
for i in range(1, 1000):
    x = int('32'+str(i)+'823')
    if x % delit == 0:
        print(x, end='   ')
        print(x // delit)