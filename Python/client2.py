import socket
import threading

host = 'localhost'
port = 12345

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # An error occurred, likely the connection was closed
            break

def send_message(client_socket, lobby_id):
    while True:
        message = input()
        full_message = f"Lobby {lobby_id}: {message}"
        client_socket.send(full_message.encode())

def connect_to_server():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((host, port))
        except:
            print("Connection failed. Retrying...")
            continue

        player_name = input("Enter your name: ")
        client_socket.send(player_name.encode())

        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()

        lobby_id = client_socket.recv(1024).decode()
        print(f"You are connected to Lobby {lobby_id}")

        send_thread = threading.Thread(target=send_message, args=(client_socket, lobby_id))
        send_thread.start()

        receive_thread.join()
        send_thread.join()

        client_socket.close()
        print("Connection closed. Retrying...")
        continue

connect_to_server()
