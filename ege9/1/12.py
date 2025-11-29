with open('12.txt') as file:
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        if all(l[x] < l[x + 1] for x in range(len(l) - 1)):
            a = sum([1 for x in l if x % 2 == 0])
            if a == len(l) - a:
                print(sum(l), l)