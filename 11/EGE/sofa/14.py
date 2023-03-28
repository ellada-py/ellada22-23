s=1331**650-55*121**610+77*11**510-3*11**100-221
x=''
count=0
while s!=0:
    if s%11==10:
        x+='a'
        count+=1
    else:
        x+=str(s%11)
    s//=11
x=x[::-1]
print(x)
print(count)