file = open('26_4.txt')
m, n = map(int, file.readline().split())
print(m, n)
l = []
for i in range(n):
    l.append(int(file.readline()))
l.sort()
mass = 0
k = []
j = 0
for i in range(n):
    if mass + l[i] <= m:
        k.append(l[i])
        mass += l[i]
    else:
        if l[i] - k[-1] <= m - mass:
            j = i
        else:
            break

print(len(k), j, n - (j + 1))


