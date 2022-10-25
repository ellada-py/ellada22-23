n=int(input('число n: '))
m=int(input('число m: '))
d=min(n,m)
while (n%d>0) or (m%d>0):
    d-=1
print('наибольший общий делитель чисел n и m: '+str(d))