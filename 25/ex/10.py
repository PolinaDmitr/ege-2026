
print(100_000 / 113)
print(113 * 885) #100005

l = []
for i in range(113, 1_000_000, 113 * 2):
    s3 = 1
    n = i + 3 ** s3
    while n < 1_000_000:
        if '0' not in str(n):
            if 99_999 < n < 1_000_000:
                l.append((n, s3))
        s3 += 1
        n = i + 3 ** s3
l.sort(key=lambda x: x[0])
print(l[:10])

s3 = [3 ** n for n in range(13)]
counter = 0
n = 99999
while counter < 5:
    n += 1
    if '0' not in str(n):
        for i in range(len(s3)):
            n13 = n - s3[i]
            if n13 > 0 and n13 % 2 == 1 and n13 % 113 == 0:
                print(n, i)
                counter += 1

