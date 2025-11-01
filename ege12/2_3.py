for n in range(501):
    s = '0' * n + '1' * n + '2' * (1000 - 2 * n)
    for x in '012':
        l = []
        for i in s:
            if i == '0':
                l.append('2')
            if i == '1':
                l.append(x)
            if i == '2':
                l.append('1')
        for i in range(1000):
            if l[i] == '0':
                l[i] = '1'
            elif l[i] == '1':
                l[i] = '2'
            elif l[i] == '2':
                l[i] = '0'
        if sum(int(k) for k in s) - 363 == sum(int(k) for k in l):
            print(x, l.count(x))