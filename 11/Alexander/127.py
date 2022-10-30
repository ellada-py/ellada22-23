list1 = []
for i in range(3):
    list1.append(int(input()))
def t(a):
    flag = False
    for i in range(1, len(a)):
        if a[i]>=a[i-1]:
            flag = True
        else:
            flag = False
            break
    if flag:
        return flag
    for i in range(1, len(a)):
        if a[i]<=a[i-1]:
            flag = True
        else:
            flag = False
            break
    if flag:
        return flag
    return flag

print(t(list1))
