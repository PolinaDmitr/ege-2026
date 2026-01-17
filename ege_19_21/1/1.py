def f(x, c):
    if x >= 37 or c > 2:
        return c == 2
    if c % 2 == 1:
        return f(x + 1, c + 1) or f(x + 2, c + 1) or f(x * 3, c + 1)
    return f(x + 1, c + 1) and f(x + 2, c + 1) and f(x * 3, c + 1)

def f2(x, c):
    if x >= 37 or c > 3:
        return c == 3
    if c % 2 == 0:
        return f2(x + 1, c + 1) or f2(x + 2, c + 1) or f2(x * 3, c + 1)
    return f2(x + 1, c + 1) and f2(x + 2, c + 1) and f2(x * 3, c + 1)

def f3(x, c):
    if x >= 37 or c > 4:
        return c == 2 or c == 4
    if c % 2 == 1:
        return f3(x + 1, c + 1) or f3(x + 2, c + 1) or f3(x * 3, c + 1)
    return f3(x + 1, c + 1) and f3(x + 2, c + 1) and f3(x * 3, c + 1)

for i in range(1, 37):
    if f(i, 0):
        print(i)
print()

for i in range(1, 37):
    if f2(i, 0):
        print(i)

print()

for i in range(1, 37):
    if f3(i, 0):
        print(i)



