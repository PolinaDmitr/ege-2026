from itertools import *

with open('20.txt') as file:
    count = 1
    res = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        lc = [x for x in l if x % 2 == 0]
        ln = [x for x in l if x % 2 != 0]
        if len(lc) == len(ln) and sum(l) % 3 == 0:
            sum3 = sum(l) / 3
            l1 = list(l)
            flag = True
            for x in range(len(l)):
                if not flag:
                    break
                for y in range(x + 1, len(l)):
                    if l[x] + l[y] == sum3:
                        print(l[x], l[y])
                        l1.remove(l[x])
                        l1.remove(l[y])
                        flag = False
                        break
            flag = True
            if len(l1) == 4:
                for x in range(len(l1)):
                    if not flag:
                        break
                    for y in range(x + 1, len(l1)):
                        if l1[x] + l1[y] == sum3:
                            print(l[x], l[y])
                            res = count
                            print(l, res)
                            flag = False
                            break
        count += 1

    print(res)

with open('20.txt') as file:
    count = 1
    res = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        lc = [x for x in l if x % 2 == 0]
        ln = [x for x in l if x % 2 != 0]
        if len(lc) == len(ln) and sum(l) % 3 == 0:
            for a in permutations(l):
                if a[0] + a[1] == a[2] + a[3] == a[4] + a[5]:
                    res = count
        count += 1

    print(res)

