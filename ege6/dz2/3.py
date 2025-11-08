def pereley(sorce: list, target: list):
    lim = target[0] - target[1]
    value = min(sorce[1], lim)
    sorce[1] = sorce[1] - value
    target[1] = target[1] + value

for n in range(100):
    a = [3, 0]
    b = [6, 0]
    c = [8, 0]
    for _ in range(n):
        print(n)
        c[1] = c[0]
        pereley(c, a)
        pereley(c, b)
        pereley(a, b)
        b[1] = 0
    pereley(a, b)
    pereley(c, b)
    print(a, b, c)
    if b[1] == 5:
        print('otv', n)
        break
