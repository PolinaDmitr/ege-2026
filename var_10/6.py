from turtle import *

tracer(0)
screensize(3000, 3000)
k = 13

# начальное положение
down()
left(90)

right(45)
for i in range(2):
    forward(k * 24)
    right(90)
    forward(k * 10)
    right(90)

forward(k * 5)
left(90)
forward(k * 12)
right(90)

for i in range(2):
    forward(k * 9)
    right(90)
    forward(k * 35)
    right(90)

up()
for x in range(-30, 50):
    for y in range(-30, 50):
        goto(x * k, y * k)
        dot(3)


update()
done()
