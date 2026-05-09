def median_x(cl):
    x = [a[0] for a in cl]
    x.sort()
    return x[len(x) // 2]

def median_y(cl):
    y = [a[1] for a in cl]
    y.sort()
    return y[len(y) // 2]

file = open('27-86a.txt')
cl1 = []
cl2 = []

for i in file.readlines():
    l = i.replace(',', '.').split()
    x = float(l[0])
    y = float(l[1])
    if x > 4:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

print(abs(median_x(cl1) + median_x(cl2)) / 2 * 10000)
print(abs(median_y(cl1) + median_y(cl2)) / 2 * 10000)