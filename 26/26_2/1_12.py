file = open('26_12.txt')
k = int(file.readline())
n = int(file.readline())

m = [0] * k

count = 0
last_k = 0

l = []
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((x, y))
l.sort()

for i in range(n):
    start, end = l[i]
    for j in range(k):
        if m[j] < start:
            m[j] = end
            count += 1
            last_k = j + 1
            break

print(count, last_k)
