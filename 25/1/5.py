# [178965; 178982]

def f(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    s.add(1)
    s.add(x)
    return s

for i in range(178_965, 178_982 + 1):
    d = f(i)
    if len(d) == 4:
        d_l = sorted(list(d), reverse=True)
        print(d_l)

# 178967 937 191 1
# 178977 59659 3 1
# 178979 2011 89 1
# 178982 89491 2 1

