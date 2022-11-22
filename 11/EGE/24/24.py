from collections import Counter
f=open('24.txt')
s=f.readline()
g=''
for i in range(len(s)-1):
    if s[i] == 'E':
        g=g+s[i+1]
print(Counter(g).most_common()[0][0])