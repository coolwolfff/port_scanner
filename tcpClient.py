import socket

HOST = '10.100.102.159'  # The remote host
PORT = 9999  # The same port as used by the server
a= input()
print("aa")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(a.encode())
data = s.recv(1024)
s.close()
print('Received', repr(data))