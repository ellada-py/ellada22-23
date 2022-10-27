a = input("Номер клетки:")
if (int(a[1])+ord(a[0]))%2==0:
    print("Клетка чёрная.")
else:
    print("Клетка белая.")
print(int(a[1]),ord(a[0]))