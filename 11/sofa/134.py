def Spisok(ar):
    res = [[]]
    for i in range(len(ar) + 1):
        for j in range(i + 1, len(ar) + 1):
            res.append(ar[i:j])
    return res
numbers = list(input('введите числа через пробел: ').split(' '))
print(Spisok(numbers))


