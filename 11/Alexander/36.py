a1 = 10.5
a2 = 4
b = int(input())
if b == 2:
    b = 2 / a1
    print(b)
elif b == 1:
    b = 1 / a1
    print(b)
elif b < 0:
    print("ОШИБКАЫЫЫЫ")
else:
    b = 2 / a1 + (b - 2) / a2
    print(b)