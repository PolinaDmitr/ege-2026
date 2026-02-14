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

left = 0
count_x = 0
count_y = 0
k_max = 0
for right in range(len(line)):
    if line[right] == 'X':
        count_x += 1
    if line[right] == 'Y':
        count_y += 1
    while count_x > 1 or count_y > 1:
        if line[left] == 'X':
            count_x -= 1
        if line[left] == 'Y':
            count_y -= 1
        left += 1
    if count_y == count_x == 1:
        k_max = max(k_max, right - left + 1)
print(k_max)