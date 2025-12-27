with open('17_1.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_max = -100_001
    for i in l:
        if -10000 < i < -999 and i % 9 == 0:
            l_max = max(l_max, i)
    m = []
    for i in range(len(l) - 1):
        l1 = int(l[i] < 0)
        l2 = int(l[i + 1] < 0)
        if l1 + l2 == 1 and l[i] + l[i + 1] > l_max:
            m.append(l[i] ** 2 + l[i + 1] ** 2)
    print(len(m), min(m))