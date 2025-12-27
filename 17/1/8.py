with open('17_8.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_max = max(i for i in l if i % 100 == 37)
    m = []
    for i in range(len(l) - 3):
        l1 = int(l[i] > l_max)
        l2 = int(l[i + 1] > l_max)
        l3 = int(l[i + 2] > l_max)
        l4 = int(l[i + 3] > l_max)
        l5 = [j for j in l[i : i + 4] if j > 9 and str(j)[-1] == str(j)[-2]]
        if l1 + l2 + l3 + l4 == 2 and len(l5) == 1:
            m.append(l5[0])
    print(len(m), sum(m), m)
