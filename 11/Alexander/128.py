list1 = []
for i in range(3):
    list1.append(int(input()))
b = int(input())
c = int(input())
def countRange(a, b, c):
    q = 0
    for i in a:
        if b<=i<c:
            q+=1
    return q
print(countRange(list1,b,c))
