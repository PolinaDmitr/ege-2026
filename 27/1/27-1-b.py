file = open('27_1_b.txt')

cl1 = []
cl2 = []
cl3 = []

for line in file.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if -20 < y < 0:
        continue
    if y < -20:
        cl1.append((x, y))
    elif x > 0:
        cl2.append((x, y))
    else:
        cl3.append((x, y))

print(len(cl1), len(cl2), len(cl3))
#cl1 - min
#cl2 - max
cl_min = min(cl1, cl2, cl3, key=len)
cl_max = max(cl1, cl2, cl3, key=len)

cl_max_x = max(x[0] for x in cl_max)
cl_min_y = max(x[1] for x in cl_min)

print(abs(cl_max_x) * 10_000)
print(abs(cl_min_y) * 10_000)
