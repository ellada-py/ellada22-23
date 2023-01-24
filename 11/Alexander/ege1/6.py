from turtle import * # Подключим модуль черепашка
color('black','red') # устанавливаем цвет пера и цвет заливки
speed(100)
lt(90)
k = 20 # коэффициент для настраивания более удобного масштаба
begin_fill()
rt(30)
for i in range(10): #указываем число циклов необходимое до полного завершения фигуры
    fd(25*k)
    rt(90)
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-100*k,100*k,k):
    for y in range(-100*k,100*k,k):
        s = canvas.find_overlapping(x,y,x,y)
        if len(s) == 1 and s[0] == 5:
            cnt+=1
print(cnt)