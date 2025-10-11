from turtle import *

tracer(0)
screensize(3000, 3000)
k = 15

left(90)
x = 27 + 3

for i in range(4):
    forward(x * k)
    right(90)
    forward(48 * k)
    right(90)
up()
forward(27 * k)
right(90)
forward(24 * k)
left(90)
down()
for i in range(4):
    forward(29 * k)
    right(90)
    back(18 * k)
    right(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(2)

update()
done()
