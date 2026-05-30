line = open('24-347.txt').readline()
s = ''
s_mn = '7'*(10**10) # так возьми сразу числовое значение, зачем эти приседания с переводом туда-сюда
s_mx = ''
k = 0 
k1 = 0
for i in line:
    if i in '01234567':     # так, а что, у нас число может начинаться на '0'?
        if s == '':
            s = i
            k1 = k     # ты k1 запоминаешь просто для каждой строчки, у тебя в ответе выводится k1 для последнего числа
            # (даже не плд условие), ты должна для подходящих чисел сохранять куда-то ещё это k1
        else:
            s+= i
            if int(s, 8) % 2 == 0:      # тут, кстати, можно просто цифру на чётность чекнуть, а не всё число, но ладно
                if len(s) > len(s_mx):
                    s_mx = s
                    #s_mn = s
                elif len(s) == len(s_mx):
                    if int(s, 8) < int(s_mn, 8):
                        s_mn = s
    else:
        s = ''
    k+=1 # так зачем вот этот ручной счётчик +1, возьми сразу в for через range

print(k1)
# 2000009

# фикс решения

s = ''
s_min_number = 10**10
s_mx = ''
k = 0
k1 = 0
for i in range(len(line)):
    if line[i] in '01234567':
        if s == '':
            if line[i] != '0':
                s = line[i]
                k1 = i
        else:
            s+= line[i]
            if int(s, 8) % 2 == 0:
                if len(s) > len(s_mx):
                    s_mx = s
                    s_min_number = int(s, 8)
                    k = k1
                elif len(s) == len(s_mx):
                    if int(s, 8) < s_min_number:
                        s_mx = s
                        s_min_number = int(s, 8)
                        k = k1
    else:
        s = ''

print(k)
