file = open('17_7.txt')
line = file.readline()

left = 0
k = 0
max_len = 0

# левый указатель на самую левую крайнюю цифру, правый указатель - на самую правую крайнюю цифру

for right in range(len(line) - 1):
    if (line[right + 1] in '*+' and line[right] in '*+') or (line[right] == '*'):
        left = right + 1
        k = 0
        continue
    # здесь компенсируем момент, что при дублях поставим левый указатель на арифметический знак
    while line[left] in '*+' and left < right:
        left += 1

    if line[right] in '+':
        k += 1
    while k > 14 and left < right:
        if line[left] in '*+':
            k -= 1
        left += 1
    if line[right] not in '*+':
        max_len = max(max_len, right - left + 1)

print(max_len)
