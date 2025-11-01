from ipaddress import *

ip_net = ip_network('143.168.72.213/255.255.255.240', False)
for i in ip_net.hosts():
    print(i)
ip_max = max(ip_net.hosts())
print(ip_max)