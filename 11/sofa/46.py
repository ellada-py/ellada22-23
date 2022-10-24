cell=input('номер клетки: ')
column=cell[0]
line=int(cell[1:])
letters='abcdefgh'
if letters.find(column)%2:
    if line%2:
        print('это белая клетка')
    else:
        print('это черная клетка')
else:
    if line%2:
        print('это черная клетка')
    else:
        print('это белая клетка')