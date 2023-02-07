def f (x):
    if x<3:
        return x
    if (x >2) and(x%2==0):
        return 3*(x-1)+f(x-1)+5
    if (x >2) and(x%2==1):
        return 3*(x+1)+f(x-2)-2
print(f(35))