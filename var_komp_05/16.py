q = [0] * 210100

for i in range(210099, -0, -1):
    if i >= 210_000:
        q[i] = i + 4
    else:
        q[i] = q[i + 3] + 2

g = [0] * 5000

for i in range(1, 5000):
    if i < 11:
        g[i] = q[i] + 6
    else:
        g[i] = g[i - 3] + 5

f = [0] * 5001

for i in range(5000, 0, -1):
    if i >= 4300:
        f[i] = g[i - 3]
    else:
        f[i] = f[i + 2] + 2

print(f[1])


