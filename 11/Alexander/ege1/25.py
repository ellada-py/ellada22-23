delit = 2079
for j in range(10):
    for i in range(1, 1000):
        x = int('33'+str(i)+'21'+str(j)+'7')
        if x % delit == 0:
            print(x, end='   ')
            print(x//delit)
