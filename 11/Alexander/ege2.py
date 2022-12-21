a = list(map(int, input().split()))
for i in range(1, len(a)-1):
    if len(a) == 0 or len(a) == 1:
        print(len(a), 'ничего')
    if a[0]*a[1] >= 0:
        print(a[0], a[1], end=' ')
        break
    if a[i]*a[i+1] >= 0:
        print(a[i], a[i-1], end=' ')
        break
    if a[i]*a[i+1] < 0:
        print(a[i], end=' ')
        break