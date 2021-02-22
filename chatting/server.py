import socket
import threading

# Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()   # getting hostname
ip = socket.gethostbyname(hostname)  # getting ip
port = 9000

server.bind((hostname, port))
server.listen()

print("Server IP : {} & Port : {}".format(ip,str(port)))

# List for clients and their names
clients = []
names = []

# Sending messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast('{} left!'.format(name).encode())
            names.remove(name)
            break

# Receiving
def receive():
    while True:
        # Accept connection
        client, address = server.accept()

        # Request and store name
        client.send('name'.encode())
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)

        # Print and broadcast name
        print("Client : {} connected with {}".format(name,str(address)))
        broadcast("{} joined!".format(name).encode())
        client.send('Connected to server!'.encode())

        # Thread for clients
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()