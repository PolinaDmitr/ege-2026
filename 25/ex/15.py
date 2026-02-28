from fnmatch import *

print(30120145 / 1917)
print(15712 * 1917) #30119904

counter = 0
pattern = '3?12?14*5'
for i in range(30_119_904, 10 ** 10, 1917):
    if fnmatch(str(i), pattern):
        print(i, i // 1917)
        counter += 1
    if counter == 5:
        break
