file = open("2.txt")
count = 0
for i in file.readlines():
    l = sorted([int(x) for x in i.split()])
    l_unique = [x for x in l if l.count(x) == 1]
    if 3 <= l.count(l[-1]) <= 4 and len(l_unique) == 8 - l.count(l[-1]):
        if l_unique[0] + l_unique[-1] <= sum(l_unique) - l_unique[0] - l_unique[-1]:
            count += 1
print(count)

file.close()