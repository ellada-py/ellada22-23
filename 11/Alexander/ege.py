a1 = open('C:\Users\Программист 5\Desktop\zadanie24_1')
"a1 = lower(a1)"

a = 2
b = 28
def f(a, b):
   if a > b or a == 22:
       return 0
   if a== b:
       return 1
   else:
       return f(a + 1, b) + f(a * 2, b) + f(a * 3, b)
print(f(2, 12) * f(12, 26))