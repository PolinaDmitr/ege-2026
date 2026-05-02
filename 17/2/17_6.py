file = open('17_6.txt')
l = []
min_68 = 10 ** 6
for i in file.readlines():
    x = int(i)
    l.append(x)
    if 0 < x < min_68 and '68' in str(x):
        min_68 = x

k = []
for i in range(len(l) - 2):
    s_m = l[i] + l[i + 1] + l[i + 2]
    if s_m >= min_68 and any(abs(x) ** 0.5 % 1 == 0 for x in l[i : i + 3]):
        k.append(s_m)

print(len(k), max(k))
