f=open('24.txt')
s=f.read()
k=1
max=0
for i in range(1, len(s)):
    if s[i] == 'P' and s[i-1] == 'P':
        k = 1
    else:
        k += 1
        if k > max:
            max = k
print(max)