import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the hostname and IP address of the machine
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print('Server IP address:', ip_address)

# set the IP address and port to listen on
ip_port = (ip_address, 9999)

# bind the socket to the IP address and port
server_socket.bind(ip_port)

# listen for incoming connections
server_socket.listen(5)
print('Waiting for client connections...')

# accept incoming connections
client_sockets = []
while len(client_sockets) < 2:
    client_socket, address = server_socket.accept()
    print(f'Connection from {address}')
    client_sockets.append(client_socket)

# chat between the clients
while True:
    # receive message from client 1 and send it to client 2
    message = client_sockets[0].recv(1024)
    if message:
        client_sockets[1].send(message)

    # receive message from client 2 and send it to client 1
    message = client_sockets[1].recv(1024)
    if message:
        client_sockets[0].send(message)