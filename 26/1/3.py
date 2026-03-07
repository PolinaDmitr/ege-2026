file = open('26_3.txt')
n, m  = map(int, file.readline().split())

l = [int(file.readline()) for x in range(n)]

l1 = []
l2 = []
for i in l:
    if 310 <= i <= 320:
        l1.append(i)
    else:
        l2.append(i)
print(sum(l1), m)
#значит, будем добирать вторым списком
l2.sort()
mass = sum(l1)
k = []
j = 0
for i in range(len(l2)):
    if mass + l2[i] <= m:
        k.append(l2[i])
        mass += l2[i]
    else:
        if l2[i] - k[-1] <= m - mass:
            j = i
        else:
            break
k[-1] = l2[j]
print(k)
print(len(l1) + len(k), sum(k) + sum(l1), m)


