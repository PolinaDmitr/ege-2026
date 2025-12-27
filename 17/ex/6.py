with open('17_6.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_max = 0
    for i in l:
        if i % 100 == 93:
            l_max = max(l_max, i)
    m = []
    for i in range(len(l) - 1):
        l1 = l[i] if l[i] > l_max else 0
        l2 = l[i + 1] if l[i + 1] > l_max else 0

        if (int(l1 != 0) + int(l2 != 0) == 1) and \
                (str(l[i])[0] == '9' or str(l[i + 1])[0] == '9'):
            m.append(l1 + l2)
    print(len(m), sum(m))
