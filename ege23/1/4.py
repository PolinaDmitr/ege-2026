def f(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    # if a == 36:
    #     return 0
    return f(a - 3, b) + f(a - 6, b) + f (a // 2, b)


print(f(86, 53) * f(53, 12))
n = f(86, 53) *f(53, 36)* f(36, 12)
print(n)
print(f(86, 53) * f(53, 12) - (f(86, 53) *f(53, 36)* f(36, 12)))