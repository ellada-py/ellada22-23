def m(n):
    max1 = 0
    max2 = 0
    for i in range(2,n):
        if n%i==0:
            k=i
            max1=n/i
            break
    for j in range (i+1,n):
        if n%j==0:
            max2=n/j
            break
    sum=max1+max2
    return sum
number=11000001

print(m(600))