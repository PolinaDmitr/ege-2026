file = open('24_10.txt')
line = file.readline()

left = 0
count_z = 0
min_len = 10 ** 10

for right in range(len(line)):
    if line[right] == 'Z':
        count_z += 1

    while count_z > 270:
        if line[left] == 'Z':
            count_z -= 1
        left += 1

    while line[left] != 'Z':
        left += 1

    if count_z == 270:
        min_len = min(min_len, right - left + 1)
        print(line[left : right + 1], right - left + 1)

print(min_len)

