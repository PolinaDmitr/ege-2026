from ipaddress import *

net = ip_network('172.16.96.0/255.255.224.0')
count = 0
for i in net:
    ip_bin = bin(int(i))[2:]
    if ip_bin.count('1') % 2 == 0:
        count += 1
print(count)