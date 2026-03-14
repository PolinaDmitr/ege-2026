file = open("26_8.txt")
n = int(file.readline())

l = dict()
for i in range(n):
    x, y = map(int, file.readline().split())
    l.setdefault(x, [])
    l[x].append(y)

print(l)

home = []
for key in l.keys():
    ents = l[key]
    ents.sort()
    if len(ents) >= 3:
        print(key, ents)
        for i in range(len(ents) - 2):
            if ents[i + 2] - ents[i] == 3:
                e = (ents[i + 2] + ents[i]) // 2 * 4 - ents[i] - ents[i + 1] - ents[i + 2]
                home.append((key, e))
                break
            if ents[i + 2] - ents[i] == 2:
                if ents.count(ents[i] - 1) == 0:
                    home.append((key, ents[i] - 1))
                elif ents.count(ents[i + 2] + 1) == 0:
                    home.append((key, ents[i + 2] + 1))

home.sort()
numbers = set([x[0] for x in home])
print(numbers)
print(home)




