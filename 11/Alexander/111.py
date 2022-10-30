a = []
b = int(input())
while b!=0:
    a.append(b)
    b = int(input())
a.sort()
a = a[::-1]
print(*a)