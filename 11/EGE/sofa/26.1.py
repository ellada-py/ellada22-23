f = open('26.txt')
s, n = map(int, f.readline().split())
v = sorted(map(int, f))
sum, cnt = 0, 0
for i in range(len(v)):
    if sum + v[i] <= s:
        sum += v[i]
        cnt += 1
biggest_file = v[cnt - 1:][0] + s - sum
while biggest_file not in v:
    biggest_file -= 1
print(cnt, biggest_file)