def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(2*x+1, y)
print(f(1, 27)-f(1,26)*f(26,27))