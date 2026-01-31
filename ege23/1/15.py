def f(a, b, command: str):
    if a == b:
        l1 = '1111111' in command and '11111111' not in command
        l2 = '2222222' in command and '22222222' not in command
        return int(l1 and l2)
    if a > b:
        return 0
    s = sum(int(x) for x in str(a))
    return f(a + 2, b, command + '1') + f(a + s, b, command + '2')


print(f(1, 70, ''))