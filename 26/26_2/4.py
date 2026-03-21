file = open('26_4.txt')
k, n = map(int, file.readline().split())
d = dict()
for i in range(k):
    k, x, y = map(int, file.readline().split())
    l = []
    for j in range(x):
        l.append([0] * y)
    # print(n, l)
    d[k] = l

for i in range(n):
    z, x, y = map(int, file.readline().split())
    d[z][x - 1][y - 1] = 1

x_min = 1000
count = 0
for key in d.keys():
    l = d[key]
    l_empty = [x for x in range(len(l)) if sum(l[x]) == 0]
    l_empty.append(len(l))
    for i in range(len(l)):
        if i + 1 not in l_empty:
            continue
        for j in range(len(l[i]) - 5):
            if sum(l[i][j : j + 5]) == 0:
                count += 1
                x_min = min(x_min, i + 1)

print(x_min, count)
#344

