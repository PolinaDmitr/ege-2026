file = open('26_11.txt')
n = int(file.readline())

d = dict()
for i in range(n):
    x, y = map(int, file.readline().split())
    d.setdefault(y, []).append(x)

c_max = 0
point_max = 0

for key in d.keys():
    l = d[key]
    l = list(set(l))
    l.sort()
    k_max = 0
    k = 1
    for i in range(len(l) - 1):
        if l[i] + 1 == l[i + 1]:
            k += 1
        else:
            k_max = max(k_max, k)
            k = 1
    if k_max > c_max:
        c_max = k_max
        point_max = key
    if k_max == c_max:
        point_max = min(key, point_max)

print(c_max, point_max)
