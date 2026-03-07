file = open('26_11.txt')
n = int(file.readline())
l = []
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((x, y))
point = {}
for i in range(n):
    x, y = l[i]
    if y not in point.keys():
        point[y] = {x}
    else:
        point.get(y).add(x)

max_p = 0
max_point = 0
for i in point.keys():
    a = list(point.get(i))
    a.sort()
    k = 1
    k_max = 1
    for u in range(len(a) - 1):
        if a[u] + 1 == a[u + 1]:
            k += 1
        else:
            k_max = max(k, k_max)
            k = 1
    if k_max > max_p:
        max_p = k_max
        max_point = i
    elif k_max == max_p:
        max_point = min(max_point, i)

print(max_p)
print(max_point)
