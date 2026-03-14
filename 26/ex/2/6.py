file = open('26_6.txt')
n = int(file.readline())

l = []
sec = set()
sec.add(0)
for i in range(n):
    x, y = map(int, file.readline().split())
    l.append((x, y))
    sec.add(x)
    sec.add(y)

sec = list(sec)
sec.sort()
l.sort()

people = [0] * (len(sec) + 1)

for i in range(len(l)):
    x, y = l[i]
    ind1 = sec.index(x)
    people[ind1] += 1
    ind2 = sec.index(y)
    people[ind2] -= 1

print(sec[-10:])
print(people[-10:])
#ну тут видно, что 1431

k_max = 0
k = 0
for i in range(len(sec) - 1):
    if people[i] == 0 and people[i + 1] == 0:
        k += sec[i + 1] - sec[i]
    else:
        k_max = max(k_max, (k + sec[i + 1] - sec[i]))
        k = 0
print(k_max)


