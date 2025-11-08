#5.2.5.0 и маской сети 255.255.0.0
from ipaddress import *

count = 0
net = ip_network('5.2.5.0/255.255.0.0', False)
for i in net:
    ip_add = bin(int(i))[2:].zfill(32)
    if ip_add.count('0') % 25 == 0:
        count += 1
print(count)
