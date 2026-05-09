file = open('24.txt')
line = file.readline()
m = []
s = ''
max_len = 1
ind = 0
for i in range(len(line)):
    if line[i] in '01234567':
        if len(s) == 0:
            if line[i] == '0':
                continue
            else:
                ind = i
        s += line[i]
        number = int(s, 8)
        if number % 13 == 0:
            m.append((s, number, ind))
            max_len = max(max_len, len(s))
    else:
        s = ''

max_len_m = [x for x in m if len(x[0]) == max_len]
max_len_m.sort(key= lambda x: x[1])
print(max_len_m[0])

