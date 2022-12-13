import random
number=random.choice([0,00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38])
print('выпавший номер: '+str(number))
print('выигравшая ставка: '+str(number))
if (number!=0) or (number!=00):
    number=int(number)
    if (number==1) or (number==3) or (number==5) or (number==7) or (number==9) or (number==12) or (number==14) or (number==16) or (number==18) or (number==19) or (number==21) or (number==21) or (number==23) or (number==25) or (number==27) or (number==30) or (number==32) or (number==34) or (number==36):
        print('выигравшая ставка: красное')
    else:
        print('выигравшая ставка: черное')
    if number % 2:
        print('выигравшая ставка: нечетное')
    else:
        print('выигравшая ставка: четное')
    if 1<=number<=18:
        print('выигравшая ставка: от 1 до 18')
    else:
        print("выигравшая ставка: от 19 до 36")