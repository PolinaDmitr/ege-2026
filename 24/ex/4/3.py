from re import *

reg = r'([.0-9A-z]*[0-9A-z])@(yandex.ru|gmail.com)'

file = open('24_3.txt')
line = file.readline()

k = []
for i in finditer(reg, line):
    k.append(i.group(0))

k_max = max(k, key=len)
print(k_max, len(k_max))