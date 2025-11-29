file = open('1.txt')
#'\n' - переход на новую строчку '\t' - табуляция
#'\r' - переведение каретки на новую строчку
count = 1
for i in file.readlines():
    l = [int(x) for x in i.split()]
    l1 = [x for x in l if l.count(x) == 1]
    if len(l) == len(l1) and 2 * (max(l) + min(l)) == 3 * (sum(l) - max(l) - min(l)):
        print(count)
    count += 1

file.close()