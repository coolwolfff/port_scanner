import socket
import time
try:
    elapsed_time=100
    UDP_IP="127.0.0.1"
    UDP_PORT= 5004
    sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(elapsed_time)
    message, addr = sock.recvfrom(1024)
    sock.sendto(message, addr)
    print("port %(t)d is free"%{"t":5004})
except TimeoutError:
    print("didnt recieve any data during %(t)d seconds" %{"t":elapsed_time})
except OSError:
    print("port %(t)d is busy"%{"t":5004})
except Exception as e:
    print("unknown error : ",e)