file = open('26-143.txt')
n = int(file.readline())
l = []
for _ in range(n):
    t, d, c = map(int, file.readline().split())
    l.append((t, d, c))

l.sort()

zap1 = []
zap2 = []

count_zap1 = 0
count_util = 0

for i in l:
    t, d, c = i

    # для заправки (t_start, t_end, del)

    zap1 = [x for x in zap1 if x[1] > t]
    zap2 = [x for x in zap2 if x[1] > t]

    if c == 1:
        if len(zap1) == 0:
            zap1.append((t, t + d, d))
            count_zap1 += 1
        elif len(zap1) < 5:
            zap1.append((zap1[-1][1], zap1[-1][1] + d, d))
            count_zap1 += 1
        else:
            count_util += 1
    if c == 2:
        if len(zap2) == 0:
            zap2.append((t, t + d, d))
        elif len(zap2) < 5:
            zap2.append((zap2[-1][1], zap2[-1][1] + d, d))
        else:
            count_util += 1
    if c == 0:
        if len(zap2) < len(zap1) and len(zap2) < 5:
            if len(zap2) == 0:
                zap2.append((t, t + d, d))
            else:
                zap2.append((zap2[-1][1], zap2[-1][1] + d, d))
        elif len(zap1) < 5:
            if len(zap1) == 0:
                zap1.append((t, t + d, d))
                count_zap1 += 1
            else:
                zap1.append((zap1[-1][1], zap1[-1][1] + d, d))
                count_zap1 += 1
        else:
            count_util += 1


print(count_zap1, count_util)