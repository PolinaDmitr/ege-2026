with open('15.txt') as file:
    count = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l1 = [l.count(x) for x in l]
        b1 = l1.count(2) == 2 and l1.count(1) == 3
        l2 = [x for x in l if x % 2 == 0]
        l3 = [x for x in l if x % 2 != 0]
        b2 = sum(l2) > sum(l3) and len(l3) != 0
        if b1 + b2 >= 1:
            count += 1
    print(count)

#13255