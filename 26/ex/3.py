file = open('26_3.txt')
s, n = map(int, file.readline().split())
print(s, n)
l = []
k = []
for i in range(s):
    a = int(file.readline())
    if 310 <= a <= 320:
        k.append(a)
    else:
        l.append(a)
print(sum(k), n)
mass = sum(k)
#узнали, что ящиков меньше
l.sort()
k2 = []
j = 0
for i in range(len(l)):
    if mass + l[i] <= n:
        k2.append(l[i])
        mass += l[i]
    else:
        #ситуация, когда у нас не одинаковые ящики - есть куда расти (можно увидеть по результату)
        if l[i] - k2[-1] <= n - mass:
            j = i
print(k2[-1], l[j])
k2[-1] = l[j]
print(len(k) + len(k2), sum(k) + sum(k2))




