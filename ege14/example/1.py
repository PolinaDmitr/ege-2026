from string import ascii_uppercase, digits

alphabet = digits + ascii_uppercase

for x in range(29):
    numb = int(f'923{alphabet[x]}874', 29) + int(f'524{alphabet[x]}6152', 29)
    if numb % 28 == 0:
        print(x, numb / 28)