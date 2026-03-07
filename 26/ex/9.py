file = open('26_9.txt')
n = int(file.readline())
print(n)
l = []
for i in range(n):
    s = file.readline().split()
    x, y = map(int, s)
    l.append((i + 1, x, y, min(x, y)))

l.sort(key=lambda x: x[3])
print(l[-1])
print('порядковый номер', l[-1][0])
l1 = []
l2 = []
for i in range(n):
    ind, x, y, m = l[i]
    if x == m:
        l1.append(l[i])
    else:
        l2.append(l[i])
#тут посмотрим, что сам телефон во втором списке
print(len(l2) - 1)
