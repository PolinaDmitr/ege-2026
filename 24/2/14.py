line = open('24_14.txt').readline()

s_count = 0
k_max = 0
left = 0

for right in range(len(line)):
    if line[right] in '02468':
        left = right
        s_count = 0
    if line[right] == 'S':
        s_count += 1

    if s_count > 35:
        left = right + 1
        s_count = 0
    if s_count == 35:
        k_max = max(k_max, right - left + 1)
print(k_max)