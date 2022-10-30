from math import *
year = int(input())
day = (year + floor((year - 1)/4) - floor((year - 1)/100) + floor((year - 1)/400))%7
b = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
print(b[day])
