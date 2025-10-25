def change(is_x_: bool, is_positive_: int):
    if not is_x_:
        is_x_ = True
    else:
        is_x_ = False
        is_positive_ *= -1
    return is_x_, is_positive_


l = []
for i in range(20):
    l.append(['_'] * 20)
x = 9
y = 9
l[x][y] = '0'
for i in l:
    print(i)

is_x = False
is_positive = 1

for i in range(10):
    for j in (5, 3, 2):
        if is_x:
            x += is_positive * j
        else:
            y += is_positive * j
        l[x][y] = '*'
        is_x, is_positive = change(is_x, is_positive)

count = 0
print()
for i in range(20):
    print(l[i])
    for j in l[i]:
        if j == '*':
            count += 1
print(count)



