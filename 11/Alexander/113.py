a = []
b = input()
while b!='':
    if b not in a:
        a.append(b)
    b = input()
for i in a:
    print(i)
