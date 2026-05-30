# для первой игры обычный вариант подойдёт (тут можно просто перебор сделать)
def f1(x, p, c):
    if x >= 125 or p > c[-1]:
        return p in c
    l = [f1(x + 2, p + 1, c),
         f1(x + 4, p + 1, c),
         f1(x * 2, p + 1, c)]
    if (p + 1) % 2 == c[0] % 2: #   тут мы болеем не за того, чей ход указываем
        return any(l)
    return all(l)

def f2(x, p, c):
    if x >= 125 or p > c[-1]:
        return p in c
    l = [f2(x + 2, p + 1, c),
         f2(x + 4, p + 1, c),
         f2(x * 2, p + 1, c)]
    if (p + 1) % 2 != c[0] % 2:
        return any(l)   # используем на игроке, за которого болеем (у кого выигрышная стратегия)
    return all(l)


for s in range(1, 125):
    if f1(s, 0, (1,)):
        print("19:", s)
        break

k = []
for s in range(1, 125):
    if f2(s, 0, (2,)):
        k.append(s)
print('20:', k[0], k[1])

# формулировка так себе, по факту нет гарантии, что Ваня проиграет 2 ходом
for s in range(1, 125):
    if f2(s, 0, (2,4,)) and not f2(s, 0, (2,)):
        print('21:', s)
        break
