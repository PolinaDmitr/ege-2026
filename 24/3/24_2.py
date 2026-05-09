file = open('24_2.txt')
line = file.readline()

s = ''
max_len = 0

for i in line:
    if i in '0123456789ABCD':
        if s == '' and i == '0':
            continue
        s += i
        if s[-1] in '02468AC':
            max_len = max(max_len, len(s))
    else:
        s = ''

print(max_len)
