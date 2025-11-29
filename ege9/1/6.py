with open('6.txt') as file:
    count = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l2 = [x for x in l if l.count(x) == 1]
        l_max = l.count(max(l))
        l2.sort()
        if 3 <= l_max <= 4 and len(l2) == 8 - l_max\
            and (l2[0] + l2[-1] <= sum(l2) - l2[0] - l2[-1]):
            count += 1
    print(count)