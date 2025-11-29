m = []
with open('1.txt') as file:
    for i in file.readlines():
        l = [int(x) for x in i.split()]
        a = [x for x in l if l.count(x) == 3]
        b = [x for x in l if l.count(x) == 1]
        if len(a) == 3 and len(b) == 4 and sum(b)/4 <= a[0]:
            print(sum(l))
            m.append(sum(l))
print()
print(m[-1])


