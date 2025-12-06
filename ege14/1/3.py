#4B3x1C7_14+5xG83F7_17
from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase
for x in range(14):
    numb = int(f'4B3{alphabet[x]}1C7', 14) + int(f'5{alphabet[x]}G83F7', 17)
    if numb % 15 == 0:
        print(x, numb / 15)
        break