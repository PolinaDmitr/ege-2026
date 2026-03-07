file = open('26_10.txt')
n = int(file.readline())
print(n)
l = []
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((i + 1, x, y, min(x, y)))
l.sort(key=lambda j: j[3])
print(l[-1])
l1 = []
l2 = []
for i in range(n):
    ind, x, y, m = l[i]
    if x == m:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(len(l2) - 1)