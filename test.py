import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(5000,65000):
    result = sock.connect_ex(('127.0.0.1',i))
    if result == 0:
        print(i," Port is open")
    else:
        print(i," Port is not open")
sock.close()