with open('3.txt') as file:
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l1 = [x for x in l if l.count(x) == 3]
        l2 = [x for x in l if l.count(x) == 1]
        if len(l1) == 3 and len(l2) == 4 and sum(l2)/4 <= l1[0]:
            print(sum(l))