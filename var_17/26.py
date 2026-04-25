file = open('26-143.txt')
n = int(file.readline())

cars = []
for _ in range(n):
    t, w, c = map(int, file.readline().split())
    cars.append((t, w, c))

cars.sort()

zap1 = []
zap2 = []
count_zap1 = 0
count_util = 0

for i in cars:
    t_start, w, c = i
    # чистим очереди
    zap1 = [x for x in zap1 if x[1] > t_start]
    zap2 = [x for x in zap2 if x[1] > t_start]

    if c == 1:
        if len(zap1) == 0:
            zap1.append((t_start, t_start + w, w, c))
            count_zap1 += 1
        elif len(zap1) < 5:
            zap1.append((zap1[-1][1], zap1[-1][1] + w, w, c))
            count_zap1 += 1
        else:
            count_util += 1
    elif c == 2:
        if len(zap2) == 0:
            zap2.append((t_start, t_start + w, w, c))
        if len(zap2) < 5:
            zap2.append((zap2[-1][1], zap2[-1][1] + w, w, c))
        else:
            count_util += 1
    else:
        if len(zap2) < len(zap1) and len(zap2) < 5:
            if len(zap2) == 0:
                zap2.append((t_start, t_start + w, w, c))
            else:
                zap2.append((zap2[-1][1], zap2[-1][1] + w, w, c))
        elif len(zap1) < 5:
            if len(zap1) == 0:
                zap1.append((t_start, t_start + w, w, c))
            else:
                zap1.append((zap1[-1][1], zap1[-1][1] + w, w, c))
            count_zap1 += 1
        else:
            count_util += 1

print(count_zap1)
print(count_util)





