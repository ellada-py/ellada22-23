import random
ticket=[]
for i in range(6):
    number=random.randint(1,49)
    ticket.append(number)
while (ticket[0] == ticket[1]) or (ticket[0]==ticket[2])or(ticket[0]==ticket[3])or(ticket[0]==ticket[4])or(ticket[0]==ticket[5])or(ticket[1]==ticket[2])or(ticket[1]==ticket[3])or(ticket[1]==ticket[4])or(ticket[1]==ticket[5])or(ticket[2]==ticket[3])or(ticket[2]==ticket[4])or(ticket[2]==ticket[5])or(ticket[3]==ticket[4])or(ticket[3]==ticket[5])or(ticket[4]==ticket[5]):
   if (ticket[0]==ticket[1])or(ticket[0]==ticket[2])or(ticket[0]==ticket[3])or(ticket[0]==ticket[4])or(ticket[0]==ticket[5]):
       ticket.remove(ticket[0])
       number=random.randint(1,49)
       ticket.append(number)
   elif  (ticket[1]==ticket[2])or(ticket[1]==ticket[3])or(ticket[1]==ticket[4])or(ticket[1]==ticket[5]):
       ticket.remove(ticket[1])
       number = random.randint(1, 49)
       ticket.append(number)
   elif  (ticket[2]==ticket[3])or(ticket[2]==ticket[4])or(ticket[2]==ticket[5]):
       ticket.remove(ticket[2])
       number = random.randint(1, 49)
       ticket.append(number)
   elif (ticket[3]==ticket[4])or(ticket[3]==ticket[5]):
       ticket.remove(ticket[3])
       number = random.randint(1, 49)
       ticket.append(number)
   elif (ticket[4]==ticket[5]):
       ticket.remove(ticket[3])
       number = random.randint(1, 49)
       ticket.append(number)
ticket.sort()
print(list(map(str,ticket)))