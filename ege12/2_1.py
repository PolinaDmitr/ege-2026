for x in range(501):
    s = '0' * (1000 - 2 * x) + '1' * x + '2' * x
    l = []
    for i in s:
        if i == '0':
            l.append('2')
        if i == '1':
            l.append('0')
        if i == '2':
            l.append('1')
    if sum(int(k) for k in s) - 178 == sum(int(k) for k in l):
        print(x)
