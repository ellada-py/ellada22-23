year=int(input('год: '))
import math
day=['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота']
i=((year+math.floor((year-1)/4)-math.floor((year-1)/100)+math.floor((year-1)/400))%7)
print(day[i])