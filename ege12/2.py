for n in range(334):
    l = '1' * (n * 2) + '2' * n + '0' * (1000 - 3 * n)
    sum1 = sum(int(x) for x in l)
    l1 = []
    for i in l:
        if i == '0':
            l1.append('2')
        elif i == '1':
            l1.append('0')
        elif i == '2':
            l1.append('1')
    sum2 = sum(int(x) for x in l1)
    if sum1 + 1640 == sum2:
        print(l)
        print(l1)
        print(l.count('0'))

for n in range(334):
    a_1 = n * 2
    a_2 = n
    a_0 = 1000 - 3 * n
    sum1 = a_0 * 0 + 1 * a_1 + 2 * a_2
    b_1 = a_2
    b_2 = a_0
    b_0 = a_1
    sum2 = b_0 * 0 + 1 * b_1 + 2 * b_2
    if sum1 + 1640 == sum2:
        print(a_0)