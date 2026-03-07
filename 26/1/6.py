file = open('26_6.txt')
n = int(file.readline())
l = []
for i in range(n):
    l.append(int(file.readline()))
l.sort(reverse=True)
group = n // 9
print('для покупателя', sum(l[group :]))
sale = 0
for i in range(8, n, 9):
    sale += l[i]
print('в итоге', sum(l) - sale)
