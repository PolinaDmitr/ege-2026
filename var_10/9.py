file = open('9.txt')
l = []
s = []
for i in range(6):
    s.append(dict())
for i in file.readlines():
    n = [int(x) for x in i.split()]

    for j in range(len(n)):
        if s[j].get(n[j]) is None:
            s[j][n[j]] = 1
        else:
            s[j][n[j]] += 1
    l.append(n)


count = 0
for i in l:
    k = 0
    for j in range(len(i)):
        if i.count(i[j]) == 1 and s[j][i[j]] > 50 and i[j] < sum(i) / len(i):
            k += 1
    if k == 1:
        count += 1

print(count)

count = 0
for i in l:
    k = 0
    for j in range(len(i)):
        if i.count(i[j]) == 1 and [i[j] for i in l].count(i[j]) > 50 and i[j] < sum(i) / len(i):
            k += 1
    if k == 1:
        count += 1

print(count)
