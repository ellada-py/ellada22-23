pi = 3
j = 2
for i in range(14):
    if i%2==0:
        pi+=(4/((j)*(j+1)*(j+2)))
    else:
        pi -= (4 / ((j) * (j + 1) * (j + 2)))
    print(pi)
    j+=2
print(pi)