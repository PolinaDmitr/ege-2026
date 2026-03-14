file = open('26_1.txt')
n = int(file.readline())

l = [int(file.readline()) for _ in range(n)]

l.sort(reverse=True)
l_count = [0] * n

for i in range(n):
    for j in range(i):
        if l[i] + 8 <= l[j]:
            l_count[i] = max(l_count[j] + 1, l_count[i])
    if l_count[i] == 0:
        l_count[i] = 1

k = max(l_count)
m = [l[x] for x in range(n) if l_count[x] == k]
print(k)
print(max(m))

