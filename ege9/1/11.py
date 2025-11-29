with open('11.txt') as file:
    count = 1
    sum_cl = 0
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        l.sort()
        if (l[0] + l[3]) ** 2 > l[1] ** 3 + l[2] ** 3 \
            and l[0] + l[3] != l[1] + l[2]:
            sum_cl += count
        count += 1
    print(sum_cl)