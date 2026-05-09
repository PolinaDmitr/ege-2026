file = open('24_8.txt')
line = file.readline()

left = 0
k = 0
max_sum = 0

for right in range(len(line) - 1):
    if (line[right] in '*+' and line[right + 1] in '*+') or line[right] in '*':
        left = right
        k = 0
        continue

    # компенсируем вариант, когда поставили на арифметический знак
    while line[left] in '+*' and left < right:
        left += 1

    if line[right] == '+':
        k += 1
    while k > 19 and left < right:
        if line[left] in '*+':
            k -= 1
        left += 1
    if line[right + 1] in '*+':
        s = line[left : right + 1]
        s_sum = sum([int(x) for x in s.split('+')])
        max_sum = max(max_sum, s_sum)

print(max_sum)