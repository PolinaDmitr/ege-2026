file = open('24_3.txt')
line = file.readline()

s = ''
s_max = ''
s_min_n = 10 * 10
k = 0

for i in range(len(line)):
    if line[i] in '0123456789AB':
        if line[i] == '0' and s == '':
            continue
        s += line[i]
        numb = int(s, 12)
        if numb % 9 == 0:
            if len(s) > len(s_max) or (len(s) == len(s_max) and numb < s_min_n):
                s_max = s
                s_min_n = numb
                k = i
    else:
        s = ''
print(s_max, k)



