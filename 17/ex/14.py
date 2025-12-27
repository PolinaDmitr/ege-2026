file = open('17_14.txt')
l = [int(x) for x in file.readlines()]
file.close()
l_max = max(i for i in l if 9 < i < 100)
l_a = []
for i in range(len(l) - 4):
    if str(l[i])[-1] == str(l[i + 1])[-1] == str(l[i + 2])[-1] == str(l[i + 3])[-1]:
        print(l[i], l[i + 1], l[i + 2], l[i + 3])
        l_a.append(l[i] + l[i + 1] + l[i + 2] + l[i + 3])
m = []
a = max(l_a)
print(a)
print()
for i in range(len(l) - 5):
    print(l[i], l[i + 1], l[i + 2], l[i + 3], l[i + 4])
    l1 = int(l[i] < a)
    l2 = int(l[i + 1] < a)
    l3 = int(l[i + 2] < a)
    l4 = int(l[i + 3] < a)
    l5 = int(l[i + 4] < a)
    sul_l = l[i] + l[i + 1] + l[i + 2] + l[i + 3] + l[i + 4]
    if (l1 + l2 + l3 + l4 + l5 == 1) and sul_l % l_max == 0:
        print(l[i], l[i + 1], l[i + 2], l[i + 3], l[i + 4])
        m.append(sul_l)
print(len(m), min(m))
