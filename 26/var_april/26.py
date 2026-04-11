file = open('26_17643.txt')
n = int(file.readline())
l = []
sum_l = 0
for _ in range(n):
    x, y, z = map(int, file.readline().split())
    l.append((x, y, z))
    sum_l += y
dor_s = sum_l / n

dorog = dict()
#key(art) - [цена, продано, осталось]
max_p = 0
for i in l:
    x, y, z = i
    if y > dor_s:
        dorog.setdefault(x, [y, 0, 0])
        if z == 0:
            dorog[x][1] += 1
            max_p = max(max_p, dorog[x][1])
        else:
            dorog[x][2] += 1
print(dorog)
print(max_p)

liders = []
for key in dorog.keys():
    x, y, z = dorog[key]
    if y == max_p:
        liders.append((key, x, y, z))
print(liders)

max2 = max([x[1] for x in liders])
l2 = [x for x in liders if x[1] == max2]
print('l2', l2)
min2 = min([x[3] for x in l2])
l3 = [x for x in l2 if x[3] == min2]

lid = l3[0]

print(lid[1] * lid[2], lid[3])

p = 0
k = 0
for i in l:
    x, y, z = i
    if x == lid[0]:
        if z == 0:
            p += y
        else:
            k += 1
print(p, k)

