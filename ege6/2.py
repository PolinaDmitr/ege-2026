from turtle import *

tracer(0)
screensize(3000, 3000)
k = 15

left(90)

for i in range(8):
    forward(16 * k)
    right(90)
    forward(22 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(8):
    forward(52 * k)
    right(90)
    forward(77 * k)
    right(90)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(2)

update()
done()

s1 = 53 * 78
s2 = 17 * 5
s3 = (23 - 5) * 5
print(s1 + s2 + s3)
