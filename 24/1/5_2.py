line = open('24_5.txt').readline()

left = 0
x_count = 0
y_count = 0
k_max = 0

for right in range(len(line)):
    if line[right] == 'X':
        x_count += 1
    if line[right] == 'Y':
        y_count += 1

    while x_count > 1 or y_count > 1:
        if line[left] == 'X':
            x_count -= 1
        if line[left] == 'Y':
            y_count -= 1
        left += 1

    if x_count == 1 and y_count == 1:
        k_max = max(k_max, right - left + 1)

print(k_max)

