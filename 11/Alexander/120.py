list1 = []
for i in range(3):
    list1.append(input())
def r(a):
    print(a[0], end = '')
    for i in range(1, len(a)):
        if i == len(a)-1:
            print(' и '+a[i])
        else:
            print(', '+  a[i], end = '')
r(list1)