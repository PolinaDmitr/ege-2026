from turtle import *

tracer(0)
screensize(3000, 3000)
k = 13

# начальное положение
down()
left(90)

for i in range(8):
    forward(k * 22)
    right(90)
    forward(k * 33)
    right(90)
up()
back(k * 8)
right(90)
forward(k * 11)
left(90)
down()
for i in range(8):
    forward(k * 73)
    right(90)
    forward(k * 62)
    right(90)

up()
for x in range(-10, 100):
    for y in range(-10, 100):
        goto(x * k, y * k)
        dot(3)


update()
done()

s1 = 22 * 33
s2 = 73 * 62
s3 = 22 * 22
print(s1 + s2 - s3)
