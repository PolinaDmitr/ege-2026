file = open('26_1.txt')
s, n = map(int, file.readline().split())
print(s, n)
l = []
for i in range(n):
    l.append(int(file.readline()))
l.sort()

m = 0
k = []
j = 0
for i in range(n):
    if m + l[i] <= s:
        k.append(l[i])
        m += l[i]
    else:
        j = i
        break
print(sum(l) - m, n - len(k))
print(sum(l[j:]), len(l[j:]))