from ipaddress import *

net = ip_network('170.180.190.200/255.255.240.0', False)
for i in net.hosts():
    ip_add_16 = hex(int(i))[2:]
    if ip_add_16[0] == ip_add_16[-1]:
        print(i)