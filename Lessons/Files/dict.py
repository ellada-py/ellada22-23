import sys
fin = open("litc-win.txt", encoding="cp1251")
for line in fin:
    s=line.split()[1]
    if len(s)>20:print(s,len(s))