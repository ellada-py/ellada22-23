t=oct(10000)
n=int(t[2:])
print(t)
print(n)
for k in range(1, len(x) - 1):
    s = int(x[2:])
    if x[k] == 4:
        if (x[k - 1] % 2 != 0) and (x[k + 1] % 2 != 0):
            n = 1
        else:
            n = 0
    else:
        n = 0