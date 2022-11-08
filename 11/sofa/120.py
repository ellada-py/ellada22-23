line=input()
list=[line]
n=''
while True:
    n += str(line)
    line=input('еще? ')
    list.append(line)
    print(n + ' и ' + str(list[-1]))
    n += ', '