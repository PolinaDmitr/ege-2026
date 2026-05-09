file = open('17_3.txt')
line = file.readline()

s = ''
len_max = 1
ind_last = 0
m = []
for i in range(len(line)):
    if line[i] in '0123456789AB':
        if s == '' and line[i] == '0':
            continue
        ind_last = i
        s += line[i]
        number = int(s, 12)
        if number % 9 == 0:
            m.append((s, number, ind_last))
            len_max = max(len(s), len_max)
    else:
        s = ''

max_len_m = [x for x in m if len(x[0]) == len_max]
min_x = min(max_len_m, key= lambda x: x[1])
print(min_x)
print(min_x[2])