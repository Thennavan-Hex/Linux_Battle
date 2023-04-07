import socket
import threading

def receive_message(client_socket):
    while True:
        message = client_socket.recv(1024)
        print(message.decode())

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the server's IP address and port
server_address = ('192.168.192.1', 9999)  # replace with the actual IP address and port

# connect to the server
client_socket.connect(server_address)

# start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
receive_thread.start()

# send messages to the server
while True:
    message = input()
    client_socket.send(message.encode())