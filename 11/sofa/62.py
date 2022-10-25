import random
nomber=int(random.choice([0,00,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]))
print('выпавший номер: '+str(nomber))
print('выигравшая ставка: '+str(nomber))
if (nomber!=0) or (nomber!=00):
    if (nomber==1) or (nomber==3) or (nomber==5) or (nomber==7) or (nomber==9) or (nomber==12) or (nomber==14) or (nomber==16) or (nomber==18) or (nomber==19) or (nomber==21) or (nomber==21) or (nomber==23) or (nomber==25) or (nomber==27) or (nomber==30) or (nomber==32) or (nomber==34) or (nomber==36):
        print('выигравшая ставка: красное')
        if nomber%2:
            print('выигравшая ставка: нечетное')
        else:
            print('выигравшая ставка: четное')
    else:
        print('выигравшая ставка: черное')
        if nomber % 2:
            print('выигравшая ставка: нечетное')
        else:
            print('выигравшая ставка: четное')
