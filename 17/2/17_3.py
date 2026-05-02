
file = open('17_2.txt')
l = []
for i in file.readlines():
    l.append(int(i))

k = []
for i in range(len(l) - 4):
    if all(0 <= x <= 255 for x in l[i : i + 4]):
        if 0 <= l[i] <= 9 and 0 <= l[i + 3] <= 9 and '1' in str(l[i + 1]) and str(l[i + 2])[0] == '2':
            k.append(sum(l[i : i + 4]))

print(len(k), max(k))