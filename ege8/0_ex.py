from itertools import *

for i in combinations('ABC', 2):    #сочетание
    print(i)
print('---------')
c = 0
for i in combinations_with_replacement('ABC', 3):
    print(i)
    c += 1
print(c)
print('---------')
for i in product('ABC', repeat=2):      #размещение с повторением
    print(i)
print('---------')
for i in permutations('ABCD'):      #перемещение (для повторения нужно отсечь)
    print(i)
print('---------')
for i in permutations('ABCD', 3):      #размещение
    print(i)