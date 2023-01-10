for i in range (174457,174506):
    count=0
    spisok=[]
    sqrt=round(i**0.5)
    for j in range (2,sqrt+1):
        if i%j==0:
            count+=1
            spisok.append(j)
            if count>2:
                break
    if count==2:
        print(i,end=' ')
        print(spisok)