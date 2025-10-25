from itertools import *

def different_sym(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


count = 0
for i in product('0123456', repeat=5):
    if i[0] != '0':
        s = ''.join(i)
        diff = different_sym(s)
        if diff and s.count('6') == 1:
            count += 1
            print(s)
print(count)

