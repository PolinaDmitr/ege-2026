file = open('26_6.txt')
n = int(file.readline())
print(n)
l = []
for i in range(n):
    l.append(int(file.readline()))
print(l)
l2 = sorted(l, reverse=True)
group = n // 9
print(sum(l) - sum(l2[:group]))
sum2 = 0
l3 = []
for i in range(8, n, 9):
    l3.append(l2[i])
    sum2 += l2[i]
print(sum(l) - sum2)