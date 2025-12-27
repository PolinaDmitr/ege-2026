with open('17_17.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_min = min(x for x in l if 99 < x < 1000 and len(set(str(x))) == 3)
    m = []
    for i in range(len(l) // 2):
        l1 = l[i]
        l2 = l[len(l) - i - 1]
        if l1 * l2 % l_min == 0:
            m.append(l1 + l2)
    print(len(m), min(m))