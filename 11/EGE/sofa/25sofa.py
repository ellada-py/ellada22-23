for i in range(45212176,50000001):
    if i % 2 == 1:
        count = 2
    else:
        count=1
    sqrtI = round(i ** 0.5)
    for j in range(2, sqrtI + 1):
        if i % j == 0:
            if j % 2 == 1:
                count += 1
            k = i // j
            if k % 2 == 1:
                count += 1
                if j == k:
                    count -= 1
            if count > 5:
                break
    if count == 5:
        print(i)