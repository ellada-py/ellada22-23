f=open('26.txt')
s=[int(i) for i in f]
max=0
while max>3:
    for i in range(1, len(s)):
        if s[i] > max:
            max = s[i]
    s.remove(max)
    max -= 3

for i in range(1,len(s)):
    if s[i]>max:
        max=s[i]
s.remove(max)
max-=3
for j in range(1,s[0]):
    if s[j]<=max-3:
