line = open('24_12.txt').readline()

c = [(-1, '')]
count = 0

for i in range(len(line) - 5):
    if i < len(line) - 9:
        if line[i : i + 9] == 'HALLOWEEN':
            c.append((i, 'HALLOWEEN'))
    if line[i : i + 5] == 'TRICK':
        c.append((i, 'TRICK'))
    if line[i : i + 5] == 'TREAT':
        c.append((i, 'TREAT'))
c.append((len(line), ''))

print(line[:100])
print(c[:100])

for i in range(len(c) - 16):
    d = {'HALLOWEEN' : 0, 'TRICK' : 0, 'TREAT' : 0}
    for j in range(i + 1, i + 16):
        d[c[j][1]] += 1
    if all(x == 5 for x in d.values()):
        count += (c[i + 1][0] - 1 - (c[i][0] + 1) + 2) * ((c[i + 16][0] + len(c[i + 16][1]) - 2) - (c[i + 15][0] + len(c[i + 15][1])) + 2)
print(count)

# 'aTRICKaghdjTREAD.....HALLOWEENghfkTREAD'
# - TREAD1[0] -> ind T -> -1 -> ind j (10)
# - TRICK[0] -> ind T -> + 1 -> ind R (2)
# - количество вариаций [ afgdh ( TREAD ] nkwej)
# - ind j - ind R + 1 -> сколько символов -> + 1 подхватить вариант с 0 символов (10)

# - TREAD2[0] -> ind T -> + 5  - 1 -> ind D -> -1 -> ind A (16)
# - HALLOWEEN[0] -> ind H -> + 9 - 1 -> ind N -> + 1 -> ind g (9)
# - ind A - ind j + 1 - сколько символов -> + 1 подхватить вариант с 0 символов (9)

