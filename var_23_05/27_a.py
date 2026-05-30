
def cent_m(cl):
    sum_m = sum(x[2] for x in cl)
    sum_xm = sum(x[0] * x[2] for x in cl)
    sum_ym = sum(x[1] * x[2] for x in cl)
    return sum_xm / sum_m, sum_ym / sum_m


file = open('27_A_28802.txt')
file.readline()
cl1 = []
cl2 = []

for i in file.readlines():
    x, y, m = map(float, i.replace(',', '.').split())
    if x > 20:
        cl1.append((x, y, m))
    else:
        cl2.append((x, y, m))

max_m = max(cl1, cl2, key=lambda x: sum(n[2] for n in x))
cent_max = cent_m(max_m)
print(cent_max[0] * 10000)
print(cent_max[1] * 10000)

