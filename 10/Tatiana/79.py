n = int(input())
m = int(input())
def ev(m,n):
    if m>n:
        m,n=n,m    # переменные обмениваются значениями. если n=2 m=3 то после этой команды n=3 m=2
    if m==0:
        return  n
    else:
        return ev(m,n-m)
print(ev(n,m))
