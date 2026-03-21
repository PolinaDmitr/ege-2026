file = open('26-155.txt')
n = int(file.readline())

d = dict()
for i in range(n):
    a, b, c = map(int, file.readline().split())
    k = (a, c)
    d[k] = d.get(k, 0) + b

b_max = 0
mark_max = (-1, -1)
for key in d.keys():
    b = d[key]
    if b > b_max:
        b_max = b
        mark_max = key
    if b == b_max:
        if key[0] > mark_max[0]:
            mark_max = key
        elif key[0] == mark_max[0] and key[1] > mark_max[1]:
            mark_max = key

print(b_max, mark_max)