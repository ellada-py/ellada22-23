import random
number=random.randint(1,49)
ticket=[number]
while len(ticket)!=6:
   for i in range(len(ticket)):
        if number==ticket[i]:
           number=random.randint(1,49)
        ticket.append(number)
ticket.sort()
print(list(map(str,ticket)))