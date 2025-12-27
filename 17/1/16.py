with open('17_16.txt') as file:
    l = [int(x) for x in file.readlines()]
    digit = 0
    l_max = 0
    for i in l:
        i_digit = len(set(str(abs(i))))
        if i > l_max and i_digit >= digit:
            l_max = i
            digit = i_digit
    print(l_max)
    m = []
    for i in range(len(l) - 2):
        l1 = [x for x in l[i : i + 3] if x >= 0 and x ** 0.5 % 1 == 0]
        if len(l1) == 1 and l[i] + l[i + 1] + l[i + 2] - l1[0] >= l_max:
            m.append(l1[0])
    print(len(m), sum(m))