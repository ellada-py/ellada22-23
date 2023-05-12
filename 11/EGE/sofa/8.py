alph=['0','1','2','3']
count=0
for q in range (1,4):
    for w in range(0, 4):
        for e in range(0, 4):
            for r in range(0, 4):
                for t in range(0, 4):
                    s=str(q)+str(w)+str(e)+str(r)+str(t)
                    if s.count('3')==1:
                        k=s.find('3')
                        if k==0:
                            if s[1]!='0':
                                count+=1
                                print(s)
                        elif k==4:
                            if s[3]!='0':
                                count+=1
                                print(s)
                        else:
                            if (s[k+1]!='0') and (s[k-1]!='0'):
                                count+=1
                                print(s)
print(count)