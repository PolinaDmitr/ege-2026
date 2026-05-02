file = open('17_17.txt')
l = []
max_2 = 0
for i in file.readlines():
    x = int(i)
    l.append(x)
    if 10 <= abs(x) <= 99 and x > max_2:
        max_2 = x

a = -10000 * 4
for i in range(len(l) - 3):
    if str(l[i])[-1] == str(l[i + 1])[-1] == str(l[i + 2])[-1] == str(l[i + 3])[-1]:
        a = max(a, sum(l[i : i + 4]))

k = []
for i in range(len(l) - 4):
    count_a = [x for x in l[i : i + 5] if x < a]
    if len(count_a) == 1 and sum(l[i : i + 5]) % max_2 == 0:
        k.append(sum(l[i : i + 5]))

print(len(k), min(k))