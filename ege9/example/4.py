file = open("4.txt")
count = 0
for i in file.readlines():
    l = [int(x) for x in i.split()]
    l1 = [x for x in l if l.count(x) > 1]
    l2 = [x for x in l if l.count(x) == 1]
    if len(l1) != 0 and len(l2) != 0 and max(l) in l2 and sum(l2) >= sum(l1) * 3:
        count += 1
print(count)



file.close()