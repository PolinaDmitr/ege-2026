file = open('26_5.txt')
n = int(file.readline())

d = dict()
for i in range(n):
    x, y, t = map(int, file.readline().split())
    d.setdefault((x, y), [])
    d[(x, y)].append(t)

key_min = ()
t_min = 10 ** 6 + 1
for i in d.keys():
    l = d[i]
    if len(l) > 1:
        l.sort()
        t_min_current = 10 ** 6
        for j in range(len(l) - 1):
            t_min_current = min(t_min_current, l[j + 1] - l[j])
        if t_min_current < t_min:
            t_min = t_min_current
            key_min = i
print(key_min, key_min[0] + key_min[1], t_min)