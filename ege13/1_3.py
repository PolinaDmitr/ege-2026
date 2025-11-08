#158.214.121.40 и сетевой маской 255.255.255.224
from ipaddress import *

net = ip_network('158.214.121.40/255.255.255.224', False)
for i in net.hosts():
    print(i)