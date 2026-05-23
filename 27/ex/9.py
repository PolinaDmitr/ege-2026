from math import dist

def cent(cl):
    cent = None
    min_d = 10 ** 10
    for p in cl:
        sum_d = sum([dist(p, p1) for p1 in cl])
        if sum_d < min_d:
            min_d = sum_d
            cent = p
    return cent


file = open('27-9b.txt')
cl1 = []
cl2 = []
cl3 = []
for i in file.readlines():
    x, y = map(float, i.replace(',', '.').split())
    if (x - 5) ** 2 + (y - 11) ** 2 < 4 ** 2:
        cl1.append((x, y))
    elif (x - 13) ** 2 + (y - 11) ** 2 < 4 ** 2:
        cl2.append((x, y))
    elif (x - 9) ** 2 + (y - 5) ** 2 < 4 ** 2:
        cl3.append((x, y))


cent_cl1 = cent(cl1)
cent_cl2 = cent(cl2)
cent_cl3 = cent(cl3)

print(abs(cent_cl1[0] + cent_cl2[0] + cent_cl3[0]) / 3 * 100_000)
print(abs(cent_cl1[1] + cent_cl2[1] + cent_cl3[1]) / 3 * 100_000)



