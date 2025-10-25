numb = 1
for i in range(10000, 100_000):
    if numb % 15 == 0:
        s = str(i)
        if all(int(s[j]) % 2 != int(s[j + 1]) % 2 for j in range(4)):
            print(s, numb)
    numb += 1
#88950
