file = open('26_1.txt')
n = int(file.readline())

l = [int(file.readline()) for _ in range(n)]
l.sort(reverse=True)

m_size = [0] * n
for i in range(1, n):
    k = l[i]
    for j in range(i):
        if l[j] - k >= 8:
            m_size[i] = max(m_size[i], m_size[j] + 1)
    if m_size[i] == 0:
        m_size[i] = 1

print(m_size)
print(m_size[-1])
print(l[m_size.index(m_size[-1])])
