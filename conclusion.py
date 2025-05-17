
import argparse
import socket

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1


def udpAnswerScanner(target,ports,message,time):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", 0))
        sock.settimeout(time)

        sock.sendto(message.encode(), (target, ports))
        receivedMessage, addr = sock.recvfrom(1024)
        print("port {} answered with the message {}".format(ports, receivedMessage.decode()))
    except TimeoutError:
        print("didnt receive any data during %(t)d seconds" %{"t":time})
    except ConnectionResetError:
        print("The target doesn't listen on port {}, so the message couldn't be sent.".format(ports))
    except OSError:
        print("port is busy")
    except Exception as e:
        print("unknown error : ",e)
def udpEcho(self):
    try:
        elapsed_time = 100
        UDP_IP = "127.0.0.1"
        UDP_PORT = 5004
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        sock.settimeout(elapsed_time)
        message, addr = sock.recvfrom(1024)
        sock.sendto(message, addr)
        print("port %(t)d is free" % {"t": 5004})
    except TimeoutError:
        print("didnt recieve any data during %(t)d seconds" % {"t": elapsed_time})
    except OSError:
        print("port %(t)d is busy" % {"t": 5004})
    except Exception as e:
        print("unknown error : ", e)
def udpAvailablePortScan(self):
    for i in range(1, 65335):
        try:
            start_time = 0
            end_time = 0
            elapsed_time = 0.0001
            UDP_IP = "127.0.0.1"
            UDP_PORT = i
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((UDP_IP, UDP_PORT))
        except TimeoutError:
            print("didnt recieve any data during %(t)d seconds" % {"t": elapsed_time})
        except OSError:
            print("port %(t)d is busy" % {"t": i})
        except Exception as e:
            print("unknown error : ", e)
def tcpScan(ip,ports):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # connecting the client
        client.connect((ip, ports))
        print("server listen on %(t)d port tcp" % {"t": ports})
        client.close()
    except:
        print("No connection could be made because the target machine actively refused it on %(t)d port tcp" % {
            "t": ports})
def synTcpScan(ip,port):
    tcpRequest = IP(dst=ip) / TCP(dport=port, flags="S")
    tcpResponse = sr1(tcpRequest, timeout=1, verbose=0)
    try:
        if tcpResponse.getlayer(TCP).flags == "SA":
            print(port, "is listening")
    except AttributeError:
        print(port, "is not listening")
def tcpEcho():
    bind_ip = "10.100.102.159"
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    while True:
        client, addr = server.accept()
        data = client.recv(1024)
        client.send(data)
        print(repr(data))
def tcpClient(ip,ports,a):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, ports))
    s.send(a.encode())
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))
def parsePorts(value):
    ports = []
    seen = set()

    for part in value.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            if start > end:
                raise argparse.ArgumentTypeError(f"Invalid range: {part}")
            for port in range(start, end + 1):
                if port in seen:
                    raise argparse.ArgumentTypeError(f"Duplicate port detected: {port}")
                seen.add(port)
                ports.append(port)
        else:
            port = int(part)
            if port in seen:
                raise argparse.ArgumentTypeError(f"Duplicate port detected: {port}")
            seen.add(port)
            ports.append(port)

    return ports
#CLI
time=3
syn=False
tcpPayload=False
parser = argparse.ArgumentParser(
                    prog='Port scanner',
                    description='The program is a network scanning tool that performs basic TCP and UDP port scans and allows for simple custom packet injection',
                    epilog='in order to start scanning ports you need to address Target IP/domain and select Port range and Protocol.\nIn order to send a packet you need to write a messege, address Target IP/domain and select Port range and Protocol.')
parser.add_argument("--ip",help="address Target IP/domain")
parser.add_argument("--port",help="select ports\nfor example:20-80,22,80,443")
parser.add_argument("--protocol",help="choose a protocol tcp or udp or both")
parser.add_argument("--payload",type=str,help="send a message, default message is hey")
parser.add_argument("--time",type=int ,help="timeout value for waiting on responses in seconds,by default set on 3 seconds")
parser.add_argument("--syn",action="store_true",help="SYN scan optinon")
parser.add_argument("--tcpPayload",type=str,help="send a payload on tcp")
args= parser.parse_args()
target=args.ip
if (args.payload ==None):
    args.payload="hey"
ports=parsePorts(args.port)
if (args.time !=None):
    time=int(args.time)
if (args.protocol=="udp"):
    for ports in ports:
        udpAnswerScanner(target,ports,args.payload,time)
if(args.protocol=="tcp"):
    if (syn):
        for ports in ports:
            tcpScan(target,ports)
    else:
        for ports in ports:
            synTcpScan(target,ports)
if(args.protocol=="both"):
    if(syn):
        for ports in ports:
            synTcpScan(target,ports)
            udpAnswerScanner(target, ports, args.payload, time)
    else:
        for ports in ports:
            tcpScan(target,ports)
            udpAnswerScanner(target, ports, args.payload, time)
if(args.tcpPayload!=None):
    for ports in ports:
        tcpClient(target,ports,args.tcpPayload)