for j in '01':
    for n in range(891):
        l = list(j * n)
        is_1 = True
        for i in range(n + 1, 891):
            l.append('1' if is_1 else '0')
            is_1 = not is_1
        is_q1 = True
        s = ''.join(l)
        for i in range(890):
            if l[i] == '0':
                if not is_q1:
                    l[i] = '1'
                is_q1 = not is_q1
            else:
                if not is_q1:
                    l[i] = '0'
                is_q1 = not is_q1
        if l.count('0') == 325:
            print(s.count('1'))