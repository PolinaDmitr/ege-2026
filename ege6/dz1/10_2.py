l = []
for i in range(3):
    l.append([x for x in range(i, i + 3)])

print(l)

for i in l:
    print(i)

print(l[1][2])