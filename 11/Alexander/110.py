a = []
b = int(input())
while b!=0:
    a.append(b)
    b = int(input())
a.sort()
print(*a)
