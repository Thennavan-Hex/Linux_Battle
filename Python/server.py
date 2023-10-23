import paramiko
import socket
import threading

# Global variable to store the game state
game_state = {"player1": None, "player2": None}

def handle_client(client):
    # Get the player's name
    client.send("Enter your name: ")
    name = client.recv(1024).strip().decode()

    # Check if there is an open player slot
    if game_state["player1"] is None:
        game_state["player1"] = name
    elif game_state["player2"] is None:
        game_state["player2"] = name
    else:
        client.send("Sorry, the game is full.")
        client.close()
        return

    # Welcome message and instructions
    client.send("Welcome, {}!\n".format(name))
    client.send("Waiting for another player to join...\n")

    # Wait for another player to join
    while game_state["player2"] is None:
        pass

    # Start the game
    client.send("The game has started!\n")
    client.send("You can now take turns making moves.\n")

    # Main game loop
    while True:
        move = client.recv(1024).strip().decode()
        if move.lower() == "quit":
            break

        # Implement your game logic here based on the 'move' received
        # For simplicity, we'll just echo the move back to the player
        client.send("You played: {}\n".format(move))

    # Cleanup after the game ends
    client.send("Thanks for playing! Goodbye.\n")
    client.close()

def main():
    host = '0.0.0.0'
    port = 2222

    # Create a new SSH server
    server = paramiko.Transport((host, port))
    server.set_gss_host(socket.getfqdn(""))
    server.load_server_moduli()

    # Generate an RSA key pair (replace this with your own key if available)
    key = paramiko.RSAKey.generate(2048)

    # Set the server's private key
    server.add_server_key(key)

    print("Server started. Listening for connections...")

    try:
        while True:
            server.listen(1)
            client, addr = server.accept()
            print("Connection established from", addr)

            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server interrupted. Shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    main()
