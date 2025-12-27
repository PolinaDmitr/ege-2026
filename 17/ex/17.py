file = open('17_17.txt')
l = [int(x) for x in file.readlines()]
file.close()
l_min = min(i for i in l if 99 < i < 1000 and len(set(str(i))) == 3)
print(l_min)
m = []
for i in range(len(l) // 2):
    l1 = l[i]
    l2 = l[len(l) - i - 1]
    if l1 * l2 % l_min == 0:
        m.append(l1 + l2)
print(len(m), min(m))
