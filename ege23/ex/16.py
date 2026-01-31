def f(a, b, track):
    if a == b and len(track) > 0:
        return 1
    if a > 49 or a < 40:
        return 0
    l = []
    if a + 1 not in track:
        l.append(f(a + 1, b, (*track, a + 1)))
    if a + 3 not in track:
        l.append(f(a + 3, b, (*track, a + 3)))
    if a - 3 not in track:
        l.append(f(a - 3, b, (*track, a - 3)))
    if a - 1 not in track:
        l.append(f(a - 1, b, (*track, a - 1)))
    return sum(l)


print(f(42, 42, tuple()))