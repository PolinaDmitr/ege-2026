q = [0] * 210_010

for i in range(210_009, 0, -1):
    if i >= 210_000:
        q[i] = i + 4
    else:
        q[i] = q[i + 3] + 2

g = [0] * 4310

for i in range(4310):
    if i < 11:
        g[i] = q[i] + 6
    else:
        g[i] = g[i - 3] + 5

f = [0] * 4310

for i in range(4309, 0, -1):
    if i >= 4300:
        f[i] = g[i - 3]
    else:
        f[i] = f[i + 2] + 2

print(f[1])