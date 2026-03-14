file = open("26_8_class.txt")
n = int(file.readline())

l = [int(file.readline()) for _ in range(n)]
l.sort(reverse=True)
print(l)

k = [l[0]]
for i in range(1, n):
    if k[-1] - 4 >= l[i]:
        k.append(l[i])

print(len(k), k[-1])