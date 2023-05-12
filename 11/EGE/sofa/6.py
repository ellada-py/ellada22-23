
count = 0
for x in range(1, 111):
    for y in range(1, 111):
        if -x / 3 ** 0.5 + 111 > y > x / 3 ** 0.5:
            count += 1
print(count)