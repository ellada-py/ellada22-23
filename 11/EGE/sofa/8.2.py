number=0
for a in range(6):
    for z in range(6):
        for l in range(6):
            for o in range(6):
                for p in range(6):
                    for b in range(6):
                        s=str(a)+str(z)+str(l)+str(o)+str(p)+str(b)
                        number+=1
                        countb=s.count('5')
                        counta=s.count('0')
                        countz=s.count('1')
                        if (countb<2) and (counta==1) and (countz<3):
                            print(s)
                            print(number)
                            break
                        break