def f(a, b, flag_25, c1):
    if a == b:
        return int(flag_25 and c1 <= 3)
    if a > b:
        return 0
    if a == 25:
        flag_25 = True
    if a in (10, 38):
        return 0
    if c1 == 3:
        return f(a + 2, b, flag_25, c1) + f(a * 3, b, flag_25, c1)
    return f(a + 1, b, flag_25, c1 + 1) + f(a + 2, b, flag_25, c1) + f(a * 3, b, flag_25, c1)


print(f(1, 43, False, 0))