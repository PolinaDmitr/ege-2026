def f(a, b, command: str):
    if a == b:
        return 1
    if a > b:
        return 0
    if command == '*':
        return f(a + 1, b, '+') + f(a + 3, b, '+')
    if command == '+':
        return f(a * 2, b, '*') + f(a * 3, b, '*')
    return 0

def f1(a, b, command: str):
    if a == b:
        return 1
    if a > b:
        return 0
    l = []
    if command != '+':
        l.append(f1(a + 1, b, '+'))
        l.append(f1(a + 3, b, '+'))
    if command != '*':
        l.append(f1(a * 2, b, '*'))
        l.append(f1(a * 3, b, '*'))
    return sum(l)


print(f(1, 9999, '+') + f(1, 9999, '*'))
print(f1(1, 9999, '0'))