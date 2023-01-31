d=149
for j in range (4):
    x=int('11'+'0'*j+'223')
    if x%d==0:
        print(x,end='   ')
        print(x//d)
for i in range (1,1000):
    x=int('11'+str(i)+'223')
    if x%d==0:
        print(x, end='   ')
        print(x // d)