grade=input('буквенная оценка: ')
letters=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
numbers=[4,4,3.7,3.3,3,2.7,2.3,2,1.7,1.3,1,0]
if grade==letters:
    for i in range(len(letters) + 1):
        if grade == letters[i]:
            print('оценка в цифрах: ' + str(numbers[i]))
            break
else:
    print('некоректный ввод')