f=open('26.txt')
s=[int(i) for i in f]
count=0
max=0

for i in range(len(s)-1):
    for j in range (i+1,len(s)):
        if s[i]%2!=0 and s[j]%2!=0:
            k=(s[i]+s[j])//2
            if k in s:
                count += 1
                if k > max:
                    max = k
print(count)
print(max)
