import socket
target_host="10.100.102.159"
target_port=9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(1,65335):
    try:
#connecting the client
        client.connect((target_host, i))
        print("server listen on %(t)d port tcp" %{"t":i})
        client.close()
    except:
        print("No connection could be made because the target machine actively refused it on %(t)d port tcp" %{"t":i})