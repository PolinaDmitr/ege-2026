from re import *

file = open('17_2.txt')
line = file.readline()

s = ''
k_max = 0
s_max = ''
for i in line:
    if i in '0123456789ABCD':
        if len(s) == 0 and i == '0':
            continue
        s += i
        if i in '02468AC':
            k = int(s, 14)
            if k > k_max:
                k_max = k
                s_max = s
    else:
        s = ''
print(len(s_max))

print('--------')

reg = r'[123456789ABCD][0123456789ABCD]*[02468AC]'
m = findall(reg, line)
m_max = max(m, key=lambda x: int(x, 14))
print(len(m_max))