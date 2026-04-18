l = []
file = open('5.txt')
for i in file.readlines():
    numbs = [int(x) for x in i.split()]
    l.append(numbs)

k = []
for i in l:
    min_numb = min(i)
    if int(min_numb ** 2 in i) + int(sum(i.count(x) // 2 for x in i) >= 3) == 1:
        k.append(sum(i))

print(min(k))