f = open('zadanie24_1.txt')
s = f.readline()
maxa = 0
for i in range(len(s)):
    if s[i] == 'A':
        k = 0
        while s[i] == 'A':
            k = k + 1
            i += 1
        if k > maxa:
             maxa = k
print(maxa)