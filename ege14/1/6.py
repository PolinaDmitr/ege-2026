#22A12E_p+2F1391_p−1H05D0_p

for p in range(18, 37):
    numb = int('22A12E', p) + int('2F1391', p) - int('1H05D0', p)
    if numb % 19 == 0:
        print(p, numb / 19)
        # break