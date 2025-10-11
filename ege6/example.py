from turtle import *

tracer(0)   #убираем анимацию
k = 20  #масштаб
screensize(3000, 3000)  #размер экрана

left(90)    #в python повёрнута вдоль оси x в mode() = "standart"
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
#рисуем свою систему координат
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * k, y * k)
        dot(5)
done() #нужно для pycharm, для idle не нужно вызывать
# update() #- можно вызвать для idle