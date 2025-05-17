import socket
import time
for i in range(1,65335):
    try:
        start_time = 0
        end_time=0
        elapsed_time=0.0001
        UDP_IP="127.0.0.1"
        UDP_PORT= i
        sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        print("port %(t)d is free"%{"t":i})
    except TimeoutError:
        print("didnt recieve any data during %(t)d seconds" %{"t":elapsed_time})
    except OSError:
        print("port %(t)d is busy"%{"t":i})
    except Exception as e:
        print("unknown error : ",e)


