import random
number=random.randint(1,49)
ticket=[number]
while len(ticket)!=6:
   for i in range(len(ticket)):
       number=random.randint(1,49)
       if number==ticket[i]:
           number=random.randint(1,49)
       else:
           ticket.append(number)
           number=random.randint(1,49)
ticket.sort()
print(list(map(str,ticket)))