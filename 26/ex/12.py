file = open('26_12.txt')
k = int(file.readline())
n = int(file.readline())
l = []
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((x, y))
l.sort()

k_last = 0
count = 0
m = [0 for _ in range(k + 1)]
for i in range(n):
    st, end = l[i]
    for j in range(1, k + 1):
        if m[j] < st:
            m[j] = end
            count += 1
            k_last = j
            break
print(k_last, count)
