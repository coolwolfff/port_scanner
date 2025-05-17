import socket
timeoutErrors = 0
connectionResetErrors = 0
try:
    elapsed_time=0.1
    UDP_IP = "127.0.0.1"
    MY_UDP_PORT = 5005
    message="abc"
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((UDP_IP, MY_UDP_PORT))
    sock.settimeout(elapsed_time)
    for i in range(5000, 6000):
        try:

            #print(i)
            sock.sendto(message.encode(), (UDP_IP, i))
            receivedMessage, addr = sock.recvfrom(1024)
            print("port {} answered with the message {}".format(i, receivedMessage.decode()))
        except TimeoutError:
            timeoutErrors = timeoutErrors + 1
            #print("didnt recieve any data during %(t)d seconds" %{"t":elapsed_time})
        except ConnectionResetError:
            connectionResetErrors += 1
#except OSError:
    #print("port is busy")
#except Exception as e:
    #print("unknown error : ",e)
except TimeoutError:
    print("didnt recieve any data during %(t)d seconds" % {"t": elapsed_time})
print("{} time ot errors, {} connection reset errors".format(timeoutErrors,connectionResetErrors))
