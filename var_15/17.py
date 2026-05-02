def f(n, osn):
    s = ''
    while n != 0:
        s = str(n % osn) + s
        n //= osn
    return s

file = open('17-418.txt')
l = []
l_6 = []
l_9 = []
for i in file.readlines():
    x = int(i)
    l.append(x)
    if len(f(x, 6)) == 4:
        l_6.append(x)
    if len(f(x, 9)) == 3:
        l_9.append(x)

min_6 = min(l_6)
min_9 = min(l_9)
print(min_6, min_9)

k = []
for i in range(len(l) - 1):
    x, y = l[i], l[i + 1]
    if x % 11 == min_6 % 5 or y % 11 == min_6 % 5:
        if x % 7 == min_9 % 13 or y % 7 == min_9 % 13:
            k.append(x + y)

print(len(k), max(k))