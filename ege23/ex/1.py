def f(a, b):
    if a == b:
        return 1
    if a < b or a == 36:
        return 0
    return f(a - 3, b) + f(a - 6, b) + f(a // 2, b)


print(f(86, 53) * f(53, 12))