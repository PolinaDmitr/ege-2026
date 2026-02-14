from re import *
line = open('24_1.txt').readline()
first_word = r'([A-Z][a-z]*)'
word = r'([A-Za-z][a-z]*)'
reg = rf'{first_word}( {word})*\.'
print(line[:500])
k = [x.group() for x in finditer(reg, line)]
print(k, max(k, key=len))
#4