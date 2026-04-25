# 126.115.78.15 и 126.115.84.26
from ipaddress import *


ip1 = ip_address('126.115.78.15')

for m in range(31, 11, -1):
    net = ip_network(f'126.115.84.26/{m}', False)
    if ip1 not in net:
        continue
    k = 0
    for i in net:
        ip_bin = bin(int(i))[2:]
        if ip_bin.count('1') == 22:
            k += 1
    print(m, k)