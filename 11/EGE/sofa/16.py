def f (x):
    if x<3:
        return 1
    if (x >2) and(x%2==1):
        return f(x-1)+f(x-2)
    if (x >2) and(x%2==0):
        sum=0
        for i in range (1,x):
            sum+=f(i)
        return sum
print(f(24))