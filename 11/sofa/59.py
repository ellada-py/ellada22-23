m='января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря','января'
data=input('введите дату: ')
probel=data.find(' ')
probel2=data.rfind(' ')
day=int(data[:probel])
month=data[probel+1:probel2]
year=int(data[probel2+1:])
if (month=='января') or (month=='марта') or (month=='мая') or (month=='июля') or (month=='августа') or (month=='октября'):
    if day<31:
        day+=1
    elif day==31:
        day=1
        n=m.index(month)
        month=m[n+1]
elif month=='февраля':
    if year % 400 == 0:
        if day<29:
            day+=1
        else:
            day=1
            n=m.index(month)
            month=m[n+1]
    elif year % 100 == 0:
        if day < 28:
            day += 1
        else:
            day = 1
            n = m.index(month)
            month = m[n + 1]
    elif year % 4 == 0:
        if day < 29:
            day += 1
        else:
            day = 1
            n = m.index(month)
            month = m[n + 1]
    else:
        if day < 28:
            day += 1
        else:
            day = 1
            n = m.index(month)
            month = m[n + 1]
elif month=='декабря':
    if day < 31:
        day += 1
    elif day == 31:
        day = 1
        n = m.index(month)
        month = m[n + 1]
        year+=1
else:
    if day < 30:
        day += 1
    elif day == 30:
        day = 1
        n = m.index(month)
        month = m[n + 1]
print('следующий день: '+str(day)+' '+month+' '+str(year))