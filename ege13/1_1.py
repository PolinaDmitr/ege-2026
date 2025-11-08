#143.168.72.213 и сетевой маской 255.255.255.240
from ipaddress import *

net = ip_network('143.168.72.213/255.255.255.240', strict=False)
for i in net.hosts():
    print(i)
#14316872222