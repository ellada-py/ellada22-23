number=0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for i in range(3):
                    s=str(a)+str(b)+str(c)+str(d)+str(i)
                    number+=1
                    if number==238:
                        print(s)
                        break