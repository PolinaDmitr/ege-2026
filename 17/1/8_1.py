p = [int(i) for i in open('17.txt')]

m = -1
for x in p:
    if x % 100 == 37 and x > m:
        m = x

k = 0
s = 0

for i in range(len(p) - 3):
    a = p[i]
    b = p[i + 1]
    c = p[i + 2]
    d = p[i + 3]

    q = [a, b, c, d]

    g = 0
    for x in q:
        if x > m:
            g += 1

    if g == 2:
        e = 0
        for x in q:
            t = x % 100
            if t >= 10 and (t // 10) == (t % 10):
                e += 1
        if e == 1:
            k += 1
            for x in q:
                t = x % 100
                if t >= 10 and (t // 10) == (t % 10):
                    s += x
                    break
print(k, s)