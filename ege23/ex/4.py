def f(a, b, flag: bool):
    if a == b:
        return int(flag)
    if a > b:
        return 0
    if a in (8, 16, 32):
        if flag:
            return 0
        return f(a + 1, b, True) + f(a + 4, b, True) + f(a * 2, b, True)
    return f(a + 1, b, flag) + f(a + 4, b, flag) + f(a * 2, b, flag)


print(f(1, 50, False))
