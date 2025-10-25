for i in range(334):
    l = list('2' * (i * 2) + '0' * i + '1' * (1000 - 3 * i))
    sum1 = sum(int(x) for x in l)
    l1 = []
    for j in l:
        if j == '0':
            l1.append('2')
        if j == '1':
            l1.append('0')
        if j == '2':
            l1.append('1')
    sum2 = sum(int(x) for x in l1)
    if sum2 == 448:
        print(l.count('1'))