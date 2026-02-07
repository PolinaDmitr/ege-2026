line = open('24_5.txt').readline()
ind_xy = []
for i in range(len(line)):
    if line[i] == 'X' or line[i] == 'Y':
        ind_xy.append(i)
k_max = 0
for i in range(len(ind_xy) - 3):
    a = ind_xy[i] + 1
    b = ind_xy[i + 3] - 1
    if line[ind_xy[i + 1]] != line[ind_xy[i + 2]]:
        k_max = max(k_max, b - a + 1)
print(k_max)