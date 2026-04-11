file = open('26_17643.txt')
n = int(file.readline())
s = 0
l = []
spr = dict()
for i in range(n):
    x, y, z = map(int, file.readline().split())
    l.append((x, y, z))
    spr[x] = [y, z]
    s += y

ss = s / n

dor = dict()
dor_ist = dict()
max_d = 0
for i in l:
    if i[1] > ss:
        if i[2] == 0:
            dor[i[0]] = dor.get(i[0], 0) + 1
            if dor[i[0]] > max_d:
                max_d = dor[i[0]]
        else:
            dor_ist[i[0]] = dor.get(i[0], 0) + 1
print(max_d)
print(dor_ist)
dor_lid = []
for key in dor.keys():
    x = dor[key]
    if x == max_d:
        dor_lid.append(key)
print(dor_lid)
max_c = max([spr[x][0] for x in dor_lid])
print(max_c)
lider = None
for i in dor_lid:
    x, y = spr[i]
    if x > max_c:
        lider = (i, x)
    elif x == max_c:
        if lider is None:
            lider = (i, x)
        elif dor_ist[i] < dor_ist[lider[0]]:
            lider = (i, x)

sum_lider = 0
k_lider = 0
for i in l:
    x, y, z = i
    if x == lider[0]:
        if z == 0:
            sum_lider += y
        else:
            k_lider += 1
print(sum_lider)
print(k_lider)


