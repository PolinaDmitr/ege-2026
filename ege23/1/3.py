def f1(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 13:
        return 0
    return f1(a + 2, b) + f1(a * 3, b) + f1(a ** 2, b)


def f2(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f2(a + 2, b) + f2(a * 3, b) + f2(a ** 2, b)


print(f1(3, 49))
print(f2(3, 49) - (f2(3, 13) * f2(13, 49)))