def f(s, c, end):
    if s >= 37 or c > end[-1]:
        return c in end
    h = [f(s + 1, c + 1, end), f(s + 2, c + 1, end), f(s * 3, c + 1, end)]
    if c % 2 != end[0] % 2:
        return any(h)
    return all(h)

for i in range(1, 40):
    if f(i, 0, (2, 4)):
        print(i)
