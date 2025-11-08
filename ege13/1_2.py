#172.16.80.0 и маской сети 255.255.248.0.
from ipaddress import *

count = 0
net = ip_network('72.16.80.0/255.255.248.0', False)
for i in net:
    ip_add = bin(int(i))[2:].zfill(32)
    if ip_add.count('1') % 2 != 0:
        count += 1
print(count, net.num_addresses)

