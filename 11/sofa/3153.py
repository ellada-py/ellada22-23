spisok=list(map(int,input().split()))
x=int(input())
spisok.sort(reverse=True)
max=0
min=201
k=-1
while k==-1:
    for i in range(len(spisok)):
        if spisok[i]>max:
            max=spisok[i]
        if spisok[i]<min:
            min=spisok[i]
    if x>max:
        k=1
        break
    elif x<min:
        k=spisok.index(min)+2
        break
    for i in range(1, len(spisok)):
        if spisok[i - 1] >= x > spisok[i]:
            k=i+1
        break
print(k)