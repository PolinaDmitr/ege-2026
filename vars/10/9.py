file = open('9.txt')
l = []
s = []
for i in range(6):
    s.append(dict())

for i in file.readlines():
    a = [int(x) for x in i.split()]
    for j in range(len(a)):
        s[j][a[j]] = s[j].get(a[j], 0) + 1
    l.append(a)

count = 0
for i in l:
    k = 0
    for j in range(len(i)):
        if i.count(i[j]) == 1 and s[j][i[j]] > 50 and i[j] < sum(i)/len(i):
            k += 1
    if k == 1:
        count += 1

print(count)
