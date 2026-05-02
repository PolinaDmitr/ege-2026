def simple(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


file = open('17_2.txt')
l = []
for i in file.readlines():
    l.append(int(i))

k = []
for i in range(len(l) - 4):
    if all(0 <= x <= 255 for x in l[i : i + 4]):
        count_simp = [x for x in l[i : i + 4] if simple(x)]
        if len(count_simp) == 2:
            k.append(sum(l[i : i + 4]))

print(len(k), max(k))