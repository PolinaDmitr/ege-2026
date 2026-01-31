def f(a, b, command: str):
    if a > b:
        return 0
    if a == b:
        f1 = '1111111' in command and '11111111' not in command
        f2 = '2222222' in command and '22222222' not in command
        return int(f1 and f2)
    sum_dig = sum(int(x) for x in str(a))
    return f(a + 2, b, command + '1') + f(a + sum_dig, b, command + '2')


print(f(1, 70, ''))