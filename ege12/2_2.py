l = list('0' * 650 + '1' * 750 + '2')
is_q0 = True
for i in range(len(l)):
    if l[i] == '2':
        if is_q0:
            l[i] = '1'
        else:
            l[i] = '0'
    elif l[i] == '1':
        l[i] = '0'
        is_q0 = not is_q0
    else:
        l[i] = '1'
        is_q0 = not is_q0
print(l.count('1'))