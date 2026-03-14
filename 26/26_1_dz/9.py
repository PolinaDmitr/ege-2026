file = open('26_9.txt')
n = int(file.readline())

l = []
for i in range(n):
    l.append(int(file.readline()))

l.sort(reverse=True)

sale = 0
for i in range(3, n, 4):
    sale += l[i] // 2
print(sum(l) - sale)

#для него не выгодно
groups = n // 4
sale2 = [x // 2 for x in l[-groups:]]
print(sum(l) - sum(sale2))