from ipaddress import *

net = ip_network('170.180.190.200/255.255.240.0', False)

k = []
for i in net.hosts():
    hex_ip = hex(int(i))[2:]
    if hex_ip[0] == hex_ip[-1]:
        k.append(i)
print(max(k))