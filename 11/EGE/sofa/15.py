a=1
while True:
    if all([(x%20==0)<=(x%11!=0) or (x+a>=300) for x in range (1,1000)]):
        print(a)
        break
    a+=1