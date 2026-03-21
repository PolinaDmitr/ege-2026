file = open('17-426.txt')
l = []
l_max = 0
for i in file.readlines():
    a = int(i)
    l.append(a)
    if a > l_max and 10000 <= abs(a) <= 99999 and abs(a) % 100 == 43:
        l_max = a