def f(x, p, end):
    if x == 0 or p > end:
        return p == end
    if p % 2 != end % 2:
        return (x >= 5 and f(x - 5, p + 1, end)) or f(x // 3, p + 1, end)
    return (x >= 5 and f(x - 5, p + 1, end)) and f(x // 3, p + 1, end)

def f2(x, p):
    # print(x, p)
    if x == 0 or p > 3:
        return p == 3
    if p % 2 == 0:
        return (x >= 5 and f2(x - 5, p + 1)) or f2(x // 3, p + 1)
    return (x >= 5 and f2(x - 5, p + 1)) or f2(x // 3, p + 1)


# for i in range(1, 50):
#     if f(i, 0, 2):
#         print(i)
# print()
for i in range(1, 50):
    if f2(i, 0):
        print(i)

# print(f2(8, 0))
