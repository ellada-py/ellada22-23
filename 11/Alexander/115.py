def qwe(a):
    list1 = [1]
    for i in range(2, int(a**0.5)+1):
        if a%i==0:
            if a//i==i:
                list1.append(i)
            else:
                list1.append(i)
                list1.append(a//i)
    return list1
a = int(input())
print(qwe(a))