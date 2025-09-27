def f(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

def f1(x):
    x_3 = f(x)
    x_3 = x_3.replace('0', '*').replace('2', '0').replace('*', '2')
    while x_3[0] == '0' and len(x_3) > 1:   #тут важно не забыть, что число может превратиться в 0, здесь убирать незначащие нули не нужно
        x_3 = x_3[1:]
    return abs(int(x_3, 3) - x)


for i in range(1, 1000):
    r = f1(i)
    if r == 378:
        print(i)
        break
