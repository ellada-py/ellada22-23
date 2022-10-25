m='января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря','января'
data=input('введите дату: ')
probel=data.find(' ')
probel2=data.rfind(' ')
day=int(data[:probel])
month=data[probel+1:probel2]
year=data[probel2+1:]
if (month=='января') or (month=='марта') or (month=='мая') or (month=='июля') or (month=='августа') or (month=='октября') or (month=='декабря'):
    if day<31:
        day+=1
    elif day==31:
        day=1
        n=m.find(month)
        month=m[n+1]
print(day)
print(month)
print(m[1])