file = open('26-150.txt')
n, m, k = map(int, file.readline().split())

l = [m] * (k + 1)

for i in range(n):
    m1, k1 = map(int, file.readline().split())
    if m1 < l[k1]:
        l[k1] = m1

max_m = 0
max_k = 0
print(l)
for i in range(1, k - 1):
    k1, k2 = l[i], l[i + 1]
    m1 = min(k1, k2) - 1
    if m1 >= max_m:
        max_m = m1
        max_k = i + 1

print(max_m, max_k)


