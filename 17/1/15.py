def f(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

with open('17_15.txt') as file:
    l = [int(x) for x in file.readlines()]
    l_max = max(x for x in l if abs(x) % 100 == 17)
    print(l_max)
    m = []
    for i in range(len(l) - 1):
        if f(l[i]) != f(l[i + 1]) and (l[i] + l[i + 1]) % l_max == 0:
            m.append(l[i] * l[i + 1])
            print(l[i], l[i + 1])
    print(len(m), max(m))
    #где-то не хватает ещё одной пары
