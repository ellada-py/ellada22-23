d=2079
for i in range (10):
    for j in range (4):
        x=int('33'+'0'*j+'21'+str(i)+'7')
        if x%d==0:
            print(x, end='   ')
            print(x//d)
    for k in range (1,100):
        if k<10:
            x=int('33'+'00'+str(k)+'21'+str(i)+'7')
            if x % d == 0:
                print(x, end='   ')
                print(x // d)
        else:
            x = int('33'+'0'+str(k)+'21'+str(i)+'7')
            if x % d == 0:
                print(x, end='   ')
                print(x // d)
    for l in range (1,1000):
        x = int('33'+str(l)+'21'+str(i)+'7')
        if x%d==0:
            print(x, end='   ')
            print(x//d)