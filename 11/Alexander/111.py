list1 = []
a = int(input())
while a!=0:
    list1.append(a)
    a = int(input())
list1.sort()
list2 = list1[::-1]
print(list2)