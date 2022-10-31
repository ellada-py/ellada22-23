larger = []
smaller = []
for i in range(4):
    larger.append(input())
for i in range(2):
    smaller.append(input())

def z(a, b):
    q = ''.join(a)
    w = ''.join(b)
    if w in q:
        return True
    else:
        return False
print(z(larger,smaller))
