from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase
print(alphabet)
#923x874_29+524x6152_29
for x in range(28, -1, -1):
    numb1 = 4 * (29 ** 0) + 7 * (29 ** 1) + 8 * (29 ** 2) + x * (29 ** 3) \
    + 3 * (29 ** 4) + 2 * (29 ** 5) + 9 * (29 ** 6)
    numb2 = 2 * (29 ** 0) + 5 * (29 ** 1) + 1 * (29 ** 2) \
    + 6 * (29 ** 3) + x * (29 ** 4) + 4 * (29 ** 5) + 2 * (29 ** 6) + 5 * (29 ** 7)
    if (numb1 + numb2) % 28 == 0:
        print(x, (numb1 + numb2) / 28)
        break

for x in range(28, -1, -1):
    numb = int(f'923{alphabet[x]}874', 29) + int(f'524{alphabet[x]}6152', 29)
    if numb % 28 == 0:
        print(x, numb / 28)
        break