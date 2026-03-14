file = open('26_4.txt')
n = int(file.readline())

l = []
for i in range(n):
    l.append(int(file.readline()))

l.sort(reverse=True)

groups = n // 3
print(sum(l[groups:]))

sale = 0
for i in range(2, n, 3):
    sale += l[i]
print(sum(l) - sale)