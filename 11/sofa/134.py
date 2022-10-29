numbers=input('введите числа через пробел: ').split(' ')
list=[[]]
k=0
while k!=len(numbers):

    for i in range(k+1):
        list+=numbers[i:k+i]
    k+=1
print(list)


