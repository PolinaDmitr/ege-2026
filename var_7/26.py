file = open('26-156.txt')
n = int(file.readline())
b = [int(x) for x in file.readline().split()]
print(b)

l = []
# сумма баллов, сумма штрафных баллов, пропуски, номер участника
for i in range(n):
    b_current = [int(x) for x in file.readline().split()]
    s = 0
    sh = 0
    k_p = 0
    for j in range(1, len(b_current)):
        result = b_current[j]
        if result == 1:
            s += b[j - 1]
        elif result == -1:
            sh += b[j - 1]
            s -= b[j - 1]
        else:
            k_p += 1
    l.append((s, sh, k_p, b_current[0]))

l.sort(key= lambda x: (-x[0], x[1], x[2], x[3]))

n_20 = n // 5

k_first = n_20
while l[k_first][0] == l[n_20 - 1][0] and l[k_first][1] == l[n_20 - 1][1] and l[k_first][2] == l[n_20 - 1][2]:
    k_first += 1
print(l[k_first])
#так можем получить первого чела + индекс от 10 % удачных
s_prise = 0
k_last = k_first
for i in range(k_first, len(l)):
    if l[i][0] > 0:
        k_last = i
# определили начало и конец, теперь отсюда 10% челым числом
n_10 = (k_last - k_first + 1) // 10
for i in range(k_first, k_first + n_10):
    s_prise += l[i][0]
print(s_prise)


