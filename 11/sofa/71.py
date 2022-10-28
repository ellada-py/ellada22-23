n1=0
pi=3
for i in range (15):
    n1+=2
    n2=n1+1
    n3=n2+1
    if i%2:
        pi-=1/(n1+n2+n3)
        print('число пи: '+str(pi))
    else:
        pi+=1/(n1+n2+n3)
        print('число пи: '+str(pi))