with open('17_14.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_a = []
    for i in range(len(l) - 3):
        if str(l[i])[-1] == str(l[i + 1])[-1] == str(l[i + 2])[-1] == str(l[i + 3])[-1]:
            l_a.append(l[i] + l[i + 1] + l[i + 2] + l[i + 3])
            # print(l[i], l[i + 1], l[i + 2], l[i + 3])
    a = max(l_a)
    l_max = max(x for x in l if 9 < abs(x) < 100)
    # print(a)
    m = []
    for i in range(len(l) - 4):
        l1 = [x for x in l[i : i + 5] if x < a]
        l_sum = sum(l[i : i + 5])
        if len(l1) == 1 and l_sum % l_max == 0:
            m.append(l_sum)
    print(len(m), min(m))