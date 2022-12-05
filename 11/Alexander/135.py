a = int(input())
list1 = []
for i in range(a + 1):
    list1.append(i)
list1[1] = 0
i = 2
while i <= a:
    if list1[i] != 0:
        j = i + i
        while j <= a:
            list1[j] = 0
            j = j + i
    i += 1
list1 = set(list1)
list1.remove(0)
print(list1)