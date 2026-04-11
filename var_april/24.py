file = open('24_28765.txt')
line = file.readline()

left = 0
k_bc = 0
k = 0

for right in range(1, len(line)):
    if line[right - 1] == 'B' and line[right] == 'C':
        k_bc += 1

    while k_bc > 180:
        if line[left] == 'B' and line[left + 1] == 'C':
            k_bc -= 1
        left += 1

    if k_bc <= 180:
        k = max(k, right - left + 1)

print(k)
