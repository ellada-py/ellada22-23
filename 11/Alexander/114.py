d = 'e'
a = input()
while a!='':
    if '-' in a:
        d = d[:d.index('e')] + a[1:] + d[d.index('e'):]
    elif a=='0':
        d = d[:d.index('e')+1]+'0'+ d[d.index('e')+1:]
    else:
        d = d + a
    a = input()
q = d.index('e')
for i in range(0, q):
    print('-', d[i], end = ',')
for i in range(q+1, len(d)):
    if i == len(d)-1:
        print(d[i], end = '.')
    else:
        print(d[i], end = ',')