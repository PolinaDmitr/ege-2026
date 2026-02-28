

l = []
for i in range(113, 1_130_000, 2 * 113):
    s_3 = 1
    n = i + 3 ** s_3
    while n < 1_000_000:
        if n > 99_999 and '0' not in str(n):
            l.append((n, s_3))
        s_3 += 1
        n = i + 3 ** s_3

l.sort()
print(l[:5])
print()

l_3 = [3 ** x for x in range(1, 13)]

n = 111_111
count = 0

while count < 5:
    if '0' in str(n):
        n += 1
        continue
    for i in range(len(l_3)):
        n_13 = n - l_3[i]
        if n_13 > 0 and n_13 % 113 == 0 and n_13 % 2 != 0:
            print(n, i + 1)
            count += 1
    n += 1


# 111142 10
# 111232 7
# 111312 8
# 111314 2
# 111322 5
