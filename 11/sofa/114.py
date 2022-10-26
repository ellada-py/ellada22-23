spisok=[]
x=input('число: ')
while x!='':
    spisok.append(int(x))
    x=input('еще?: ')
for i in range(len(spisok)):
    n=spisok[i]
    if n<0:
        print(n)
for i in range(len(spisok)):
    n=spisok[i]
    if n==0:
        print(n)
for i in range(len(spisok)):
    n=spisok[i]
    if n>0:
        print(n)