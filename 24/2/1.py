from re import *
line = open('24_1.txt').readline()
print(line[:100])
first_word = r'([A-Z][a-z]*)'
word = r'([A-Za-z][a-z]*)'
pattern = rf'{first_word}(?: {word})*\.'
k = [x.group() for x in finditer(pattern, line)]
print(k)
k_max = max(k, key=len)
print(k_max)
#You are a genius.