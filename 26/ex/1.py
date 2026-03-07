file = open('26_1.txt')
s, n = map(int, file.readline().split())
print(s, n)
l = []
for i in range(n):
    l.append(int(file.readline()))
l.sort()
s2 = 0
j = 0
for i in range(n - 1):
    if s2 + l[i] <= s:
        s2 += l[i]
    else:
        j = i
        break
print(n - j, sum(l[j:]))
#возможно, последние контейнеры можно как-то подменить между друг другом

