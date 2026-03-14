file = open('26_3.txt')
n = int(file.readline())

#чисто, чтобы на всякий сохранить
l = []
d = dict()
for i in range(n):
    n, h, e = map(int, file.readline().split())
    l.append((n, h, e))
    d.setdefault(h, []).append(e)

d2 = dict()


max_len = 0
for key in d.keys():
    ents = d[key]
    ents.sort()
    k = 1
    k_max = 1
    e_min = -1
    e_start = ents[0]
    for i in range(len(ents) - 1):
        if ents[i] + 1 == ents[i + 1]:
            k += 1
        else:
            if k > k_max:
                e_min = e_start
                k_max = k
            e_start = ents[i + 1]
            k = 1
    max_len = max(max_len, k_max)
    if k_max > 1:
        d2[key] = (k_max, e_min)

print(max_len)
for i in d2.keys():
    h = d2[i]
    if h[0] == max_len:
        print(i, h)
        for j in l:
            if j[1] == i and j[2] == h[1]:
                print(j)

