f=open('zadanie24_1.txt')
s=f.read()
max=0
count=0
for i in range (len(s)):
    if s[i]=='C':
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)