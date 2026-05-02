file = open('17_18.txt')

l = []
min_3 = 10 ** 7
for i in file.readlines():
    x = int(i)
    l.append(x)
    x_abs = str(abs(x))
    if 100 <= abs(x) <= 999 and x_abs[0] != x_abs[1] and x_abs[1] != x_abs[2] and x_abs[0] != x_abs[2]:
        min_3 = min(min_3, x)
        print(x)

k = []
for i in range(len(l) // 2):
    x, y = l[i], l[-(i + 1)]
    if x * y % min_3 == 0:
        k.append(x + y)

print(len(k), min(k))

