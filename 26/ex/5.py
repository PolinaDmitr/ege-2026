file = open('26_5.txt')
n, v = map(int, file.readline().split())
print(n, v)
l1 = []
l2 = []
for i in range(n):
    a = int(file.readline())
    if 7000 <= a <= 12000:
        l1.append(a)
    else:
        l2.append(a)
print(sum(l1) / 1000, v)
#значить, l2 не волнует
v = v * 1000
l1.sort(reverse=True)
print(l1)
k = []
mass = 0
for i in range(len(l1)):
    if mass + l1[i] <= v:
        k.append(l1[i])
        mass += l1[i]
print(len(k), min(k))