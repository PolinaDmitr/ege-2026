for n in range(1001):
    is_q0 = True
    l = ['0'] * n + ['1'] * (1000 - n)
    for i in range(1000):
        if l[i] == '0':
            if not is_q0:
                l[i] = '1'
            is_q0 = False
        else:
            l[i] = '0'
            is_q0 = True
    if l.count('0') == 100:
        print(n)