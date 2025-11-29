with open('2.txt') as file:
    count = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l.sort()
        l1 = [x for x in l if l.count(x) == 1]
        if len(l) == len(l1) and l[0] * l[1] <= sum(l[2:]):
            count += 1
    print(count)
