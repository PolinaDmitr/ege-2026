def f(a, b, flag_30: bool, command: str):
    if a > b + 2:
        return 0
    if a == b:
        return int(flag_30)
    if a == 30:
        flag_30 = True
    if a == 20:
        return 0
    if command == 'A':
        return f(a + 2, b, flag_30, 'B') + f(a * 2, b, flag_30, 'C')
    return f(a - 1, b, flag_30, 'A') + f(a + 2, b, flag_30, 'B') + f(a * 2, b, flag_30, 'C')


print(f(3, 40, False, '0'))