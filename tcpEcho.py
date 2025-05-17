import socket
bind_ip = "127.0.0.1"
bind_port = 5004
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
while True:
    client, addr = server.accept()
    data = client.recv(1024)
    client.send(data)
    print(repr(data))