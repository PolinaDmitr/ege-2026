def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


file = open('17_1.txt')
l = []
for i in file.readlines():
    l.append(int(i))

k = []
for i in range(len(l) - 4):
    if all(0 <= x <= 255 for x in l[i : i + 4]):
        count_1 = bin(l[i]).count('1') + bin(l[i + 1]).count('1') + bin(l[i + 2]).count('1') + bin(l[i + 3]).count('1')
        if simple(count_1):
            k.append(sum(l[i : i + 4]))

print(len(k), max(k))