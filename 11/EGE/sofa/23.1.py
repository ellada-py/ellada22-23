def f (x,y):
    if x==y:
        return 1
    if x<y:
        return 0
    return f(x-1,y)+f(x//2,y)
print(f(60,20)*f(20,1)-f(60,20)*f(20,4)*f(4,1))