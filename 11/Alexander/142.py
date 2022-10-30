a = input()
asd = {}
for i in a:
    if i not in asd.keys():
        asd[i]=i
print(len(asd.keys()))