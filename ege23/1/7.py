def f(a, b, command: str):
    if a > b:
        return 0
    if a == b:
        return 1
    if command == 'A':
        return f(a + 3, b, 'A') + f(a * 7, b, 'C')
    return f(a + 3, b, 'A') + f(a * 5, b, 'B') + f(a * 7, b, 'C')


print(f(1, 1000, '0'))