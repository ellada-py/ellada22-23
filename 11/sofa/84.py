import random
coin=''
for i in range(10):
    while (coin.find('О О О')!=0) or (coin.find('Р Р Р')!=0):
        side=random.choice(['О','Р'])
        coin+=side
print(coin)
