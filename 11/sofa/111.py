spisok=[]
x=int(input('число: '))
while x:
    spisok.append(x)
    x=int(input('еще?: '))
spisok.sort(reverse=True)
print('\n'.join(list(map(str,spisok))))