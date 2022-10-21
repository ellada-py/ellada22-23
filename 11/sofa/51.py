a=int(input('коэфицент a: '))
b=int(input('коэфицент b: '))
c=int(input('коэфицент c: '))
if a==0:
    if b==0:
        if c==0:
            print('x-любое число')
        else:
            print('решений нет')
    else:
        print('x='+str(-c/b))
else:
    if b==0:
        if c==0:
            print('x=0')
        else:
            print('x='+str((-c/a)**0.5)+' ; '+str(-(-c/a)**0.5))
    else:
        if c==0:
            print('x=0 ; '+str(-b/a))
        else:
            d=b**2-4*a*c
            if d<0:
                print('корней нет')
            elif d==0:
                print('x='+str(-b/2*a))
            else:
                print('x='+str((-b+d**0.5)/2*a)+' ; '+str((-b-d**0.5)/2*a))