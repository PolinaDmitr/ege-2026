from string import digits, ascii_uppercase, ascii_lowercase

alphabet = digits + ascii_uppercase + ascii_lowercase

#504_6 = 5 * 6 ** 2 + 0 * 6 ** 1 + 4 * 6 ** 0
def f(s_, a_):
    res = 0
    step = len(s_) - 1
    for i in range(len(s_)):
        res += alphabet.find(s_[i]) * a_ ** (step - i)
    return res


#J569x_42+1xIA_42
for x in range(42):
    numb = f(f'J569{alphabet[x]}', 42) + f(f'1{alphabet[x]}IA', 42)
    if numb % 155 == 0:
        print(x, numb / 155)
        break