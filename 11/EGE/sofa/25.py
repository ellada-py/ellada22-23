d=123
for j in range (4):
    x=int('32'+'0'*j+'823')
    if x%d==0:
        print(x,end='   ')
        print(x//d)
for k in range(1,100):
    if k < 10:
        x=int('32'+'00'+str(k)+'823')
        if x % d == 0:
            print(x, end='   ')
            print(x // d)
    else:
        x=int('32'+'0'+str(k)+'823')
        if x % d == 0:
            print(x, end='   ')
            print(x // d)
for i in range (1,1000):
    x=int('32'+str(i)+'823')
    if x%d==0:
        print(x, end='   ')
        print(x // d)