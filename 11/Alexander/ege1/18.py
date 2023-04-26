xa = int((111 * 3**0.5) / 2)
counter = 0
for x in range(1, xa):
    for y in range(1, 111):
        y1 = x / 3 ** 0.5
        y2 = -x / (3 ** 0.5) + 111
        if y1 < y < y2:
            counter+=1
print(counter)