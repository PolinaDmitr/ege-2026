from re import findall

# 8902??&
p2 = [2 ** x for x in range(1, 15)]

l = []
for a1 in '0123456789':
    for a2 in '0123456789':
        for a3 in p2:
            numb = int(f'8902{a1}{a2}{a3}')
            if numb % 1432 == 0 and numb < 10 ** 10:
                l.append(numb)
l.sort()
for i in l:
    print(i , i // 1432)

print()
reg = r'^8902[0-9][0-9][0-9]*'

start = 8902001 // 1432 * 1432
for i in range(start, 10 ** 10, 1432):
    s = str(i)
    if len(findall(reg, s)) > 0 and s[6] != '0':
        p_n = int(s[6:])
        if p_n in p2:
            print(i, i // 1432)