file = open('26_2.txt')
n = int(file.readline())
l = []
for i in range(n):
    l.append(int(file.readline()))
l.sort(reverse=True)

k = [l[0]]
for i in range(1, n):
    if k[-1] - l[i] >= 9:
        k.append(l[i])

print(len(k), k[-1])