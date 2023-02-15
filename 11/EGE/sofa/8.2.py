number=0
for k in range(6):
    for n in range(6):
        for o in range(6):
            for r in range(6):
                for c in range(6):
                    for i in range(6):
                        s=str(k)+str(n)+str(o)+str(r)+str(c)+str(i)
                        number+=1
                        countk=s.count('0')
                        counti=s.count('5')
                        if (countk<=3) and (counti==2):
                            print(s)
                            print(number)
                            break
                        break