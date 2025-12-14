#ДЕЛ(х,128)→(¬ДЕЛ(х,А)→¬ДЕЛ(х,80))
def f(x_, a_):
    return (x_ % 128 == 0) <= ((x_ % a_ != 0) <= (x_ % 80 != 0))

for a in range(1, 1000):
    flag = True
    for x in range(1, 50000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
