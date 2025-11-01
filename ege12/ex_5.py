for n in range(501):
    s = '0' * n + '1' * n + '2' * (1000 - 2 * n)
    l = []
    for i in s:
        if i == '0':
            l.append('2')
        if i == '1':
            l.append('x')
        if i == '2':
            l.append('1')
    for j in '123':
        s2 = ''.join(l).replace('x', j)
        l2 = []
        for i in s2:
            if i == '0':
                l2.append('1')
            elif i == '1':
                l2.append('2')
            elif i == '2':
                l2.append('0')
        if sum(int(x) for x in s) == sum(int(x) for x in l2) + 363:
            print(l.count(f'{j}'))
