a = input("по вертикали:")
b = int(input("по горизонтали: "))
if a == 'a' or 'c' or 'g' or 'e':
    if b % 2 == 0:
        print("белая")
    else:
        print("черная")
else:
    if b % 2 == 0:
        print("черная")
    else:
        print("белая")