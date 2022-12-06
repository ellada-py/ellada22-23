f=open('27-B_2.txt')
a=[int(i) for i in f]
max=0
max2=0
for j in range(1,a[0]+1):
    if a[j]>max:
        max=a[j]
print(max)
a.remove(max)
if max%14==0:
    for l in range (1,a[0]):
        if a[l]>max2:
            max2=a[l]
else:
    for k in range(1,a[0]):
        if a[k]%14==0:
            if a[k]>max2:
                max2=a[k]
print(max2)
print(max*max2)