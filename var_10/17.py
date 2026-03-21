file = open('17-426.txt')

l = []
for i in file.readlines():
    l.append(int(i))

max_l = max([x for x in l if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 43])

k = []
for i in range(len(l) - 2):
    for j in (l[i], l[i + 1], l[i + 2]):
        if 10000 <= abs(j) <= 99999 and abs(j) % 100 == 43:
            sum_l = l[i] ** 2 + l[i + 1] ** 2 + l[i + 2] ** 2
            if sum_l <= max_l ** 2:
                k.append(sum_l)
                break
print(min(k), len(k))

