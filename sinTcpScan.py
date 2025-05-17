#import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1

ip="127.0.0.1"
port=5004
tcpRequest = IP(dst=ip)/TCP(dport=port,flags="S")
tcpResponse = sr1(tcpRequest,timeout=1,verbose=0)
try:
    if tcpResponse.getlayer(TCP).flags == "SA":
        print(port,"is listening")
except AttributeError:
    print(port,"is not listening")
