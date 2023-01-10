a = 4**2018+2**2018-32
c = 0
while a != 0:
    b = a % 2
    a = a//2
    if b == 1:
        c += 1
print(c)
