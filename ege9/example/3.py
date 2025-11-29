file = open('3.txt')
for i in file.readlines():
    l = [int(x) for x in i.split()]
    l_sort = sorted(l)
    if l == l_sort:
        print(l, l_sort)




file.close()