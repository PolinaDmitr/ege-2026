from itertools import *

count = 0
for i in product('ДИОНСЙ', repeat=6):
    s = ''.join(i)
    if ('Д' in s) != ('Н' in s):
        l = ('ДД', 'НН', 'ИИ', 'ОО', 'СС', 'ЙЙ')
        if all(x not in s for x in l):
            count += 1
print(count)