s=9**8*3**20-3**10-3
print(s)
x=[]
count=0
while s!=0:
    x+=str(s%3)
    s=s//3
x=x[::-1]
for i in range (len(x)):
    if x[i]=='2':
        count+=1
print(x)
print(count)