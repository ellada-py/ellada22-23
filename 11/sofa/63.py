n=int(input())
a=0
k=0
if n==0:
    print('первое число не может равнятся 0')
else:
    while (n>0) or (n<0):
        a += n
        k += 1
        n = int(input())
    print('среднее арифметическое чисел: '+str(a/k))