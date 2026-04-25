line = open('24-337.txt').readline()
s_mx = ''
s = ''
for i in line:
    if i in '0123456789ABCD':
        if s == '' and i != '1':
            continue
        else:
            s += i
            if len(s) > len(s_mx) and int(s, 14) % 7 == 0:  #не обязательно самая длинная строчка будет кратна 7, нужно проверять каждую
                s_mx = s
    else:
        s = ''

print(len(s_mx))
print(s_mx)