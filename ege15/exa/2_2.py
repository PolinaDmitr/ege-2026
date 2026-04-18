from math import lcm

def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


print(f(22229))
print(f(22247))
print(22229 * 22247)
print(lcm(22229, 22247))

print(f(17))
print(f(53))
print(90_000_000 - 17 * 53)
print(f(404))
print(lcm(115, 78, 51))
print(115 * 78 * 51)