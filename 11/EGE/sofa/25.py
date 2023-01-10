count = 0
number = 500000001
while count < 5:
    i = number // 2
    dell = 1
    count1 = 0
    for j in range(2, i + 1):
        if number % j == 0:
            count1 += 1
            dell *= j
            if dell > number:
                break
            elif count1 == 5:
                print(dell)
                count += 1
                break
    number += 1