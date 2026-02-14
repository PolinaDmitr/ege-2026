line = open('24_6.txt').readline()
y_max = 0
y_len = len(line)
x_ind = [x for x in range(len(line)) if line[x] == 'X']
for i in range(len(x_ind) - 1):
    l = line[x_ind[i] : x_ind[i + 1] + 1]
    if l.count('Y') > y_max:
        y_len = len(l)
        y_max = l.count('Y')
    elif l.count('Y') == y_max:
        y_len = min(y_len, len(l))
print(y_max, y_len)
