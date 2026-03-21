file = open('26-155.txt')
n = int(file.readline())

d = dict()
for i in range(n):
    a, b, c = map(int, file.readline().split())
    # d.setdefault((a, c), 0)
    # d[(a, c)] += b
    key = (a, c)
    d[key] = d.get(key, 0) + b

max_fine = 0
max_mark = (-1, -1)
print(d)

for i in d.keys():
    s = d[i]
    if s > max_fine:
        max_fine = s
        max_mark = i
    if s == max_fine:
        if i[0] > max_mark[0]:
            max_mark = i
        if i[0] == max_mark[0] and i[1] > max_mark[1]:
            max_mark = i

print(max_fine, max_mark)