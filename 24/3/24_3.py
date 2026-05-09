file = open('24_3.txt')
line = file.readline()

s = ''
m = []
max_len = 0

for i in range(len(line)):
    if line[i] in '0123456789AB':
        if s == '' and line[i] == '0':
            continue
        s += line[i]

        number = int(s, 12)
        if number % 9 == 0:
            m.append((s, number, i))
            max_len = max(max_len, len(s))
    else:
        s = ''

m_max_len = [x for x in m if len(x[0]) == max_len]
min_m = min(m_max_len, key= lambda x: x[1])
print(min_m)
print(min_m[2])
