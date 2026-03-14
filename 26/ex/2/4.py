file = open('26_4.txt')
n, k = map(int, file.readline().split())
zal = dict()
d = dict()
for i in range(n):
    ind, x, y = map(int, file.readline().split())
    zal[ind] = (x, y)
    l = []
    for j in range(x):
        l.append([0] * y)
    d[ind] = l
for i in range(k):
    ind, x, y = map(int, file.readline().split())
    l = d[ind]
    l[x - 1][y - 1] = 1

print(d[1])

c = 0
min_x = 100000

for key in d.keys():
    l = d[key]
    empty_l = [x for x in range(len(l)) if sum(l[x]) == 0]
    print(key, empty_l)
    for i in range(len(l) - 1):
        for j in range(len(l[i]) - 5):
            if sum(l[i][j : j + 5]) == 0 and (i + 1) in empty_l:
                c += 1
                min_x = min(min_x, i + 1)
                print(key, i, j)
    last = len(l) - 1
    for j in range(len(l[0]) - 5):
        if sum(l[last][j: j + 5]) == 0:
            c += 1
            min_x = min(min_x, last + 1)
            print(key, last, j)


print(c, min_x)

