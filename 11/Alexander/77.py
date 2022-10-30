list1 = []
for i in range(1,11):
    list1.append(i)
print(' ', *list1)
for i in range(1,11):
    print(i, end = ' ')
    for j in list1:
        print(i*j, end =' ')
    print(end = '\n')
