file = open('26_9.txt')
n = int(file.readline())
l = []
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((i + 1, x, y, min(x, y)))
l.sort(key=lambda x: x[3])
print(l[-1], l[-1][0])
l1 = []
l2 = []
for i in range(n):
    ind, x, y, m = l[i]
    if x == m:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(len(l2) - 1)
l_result = l1 + l2[::-1]
print(l_result)
