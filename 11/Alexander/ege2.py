a = list(map(int, input().split()))
for i in range(1, len(a)):
    if a[i] >= 0 and a[i+1: -1] >= 0 and a[i - 1] >= 0:
        print(a[i], a[i+1], end=' ')
    if a[i] < 0 and a[i+1:-1] < 0 and a[i - 1] < 0:
        print(a[i], end=' ')