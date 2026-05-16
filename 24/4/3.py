from re import finditer

file = open('24_3.txt')
line = file.readline()

reg = r'(([0-9A-z.]*[0-9A-z])@(yandex.ru|gmail.com))'

k = []
for i in finditer(reg, line):
    k.append(i.group(0))

k_max = max(k, key=len)
print(k_max, len(k_max))