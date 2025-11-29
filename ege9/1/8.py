with open('8.txt') as file:
    count = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l_sorted = sorted(l)
        l_min = min(l)
        l_max = max(l)

        b1 = l.count(l_max) == 1
        b2 = l[0] != l_min and l[0] != l_max and l[-1] != l_max and l[-1] != l_min
        p3 = l_sorted[-1] * l_sorted[-2] * l_sorted[-3]
        b3 = p3 % l_min == 0

        if int(b1) + int(b2) + int(b3) == 1:
            count += 1
    print(count)