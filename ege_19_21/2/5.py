def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# def f1(x, p, c):
#     if f(x) or p > c:
#         return p == c