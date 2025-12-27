with open('17_5.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_max = max(i for i in l if abs(i) % 100 == 25)
    m = []
    for i in range(len(l) - 2):
        l1 = int(999 < abs(l[i]) < 10000)
        l2 = int(999 < abs(l[i + 1]) < 10000)
        l3 = int(999 < abs(l[i + 2]) < 10000)
        l_sum = l[i] + l[i + 1] + l[i + 2]
        if l1 + l2 + l3 <= 2 and l_sum <= l_max:
            m.append(l_sum)
    print(len(m), max(m))