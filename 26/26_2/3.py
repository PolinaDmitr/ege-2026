file = open('26_3.txt')
n = int(file.readline())

l = []
d = dict()
d2 = dict()
for i in range(n):
    num, h, e = map(int, file.readline().split())
    l.append((num, h, e))
    d.setdefault(h, set()).add(e)
    d2.setdefault(e, []).append(num)

# print(d)
l2 = []

h_max = 1
numb_h = 0

for key in d.keys():
    ent = list(d[key])
    ent.sort()
    k_max = 1
    ent_min = 0
    ent_current = 0
    k = 1
    for i in range(len(ent) - 1):
        if ent[i] + 1 == ent[i + 1]:
            k += 1
        else:
            if k > k_max:
                k_max = k
                ent_min = ent_current
            ent_current = ent[i + 1]
            k = 1
    l2.append((key, k_max, ent_min))
    if h_max < k_max:
        h_max = k_max

# print(l2)
l3 = [x for x in l2 if x[1] == h_max]
print(l3)
print(min(d2[805]), min(d2[701]))

