#(x&A=0)→((x&77=0)∧(x&44=0))
def f(x_, a_):
    return (x_ & a_ == 0) <= ((x_ & 77 == 0) and (x_ & 44 == 0))

for a in range(1, 10000):
    if all(f(x, a) for x in range(1, 5000)):
        print(a)
        break
print()







print(bin(5)[2:].zfill(5))
print(bin(8)[2:].zfill(5))
print(bin(5 & 8)[2:].zfill(5))
print(bin(5 | 8)[2:].zfill(5))
print(bin(5 ^ 8)[2:].zfill(5))
