import socket

server = socket.socket()

host = socket.gethostname()   # getting hostname
ip = socket.gethostbyname(host)   # getting ip
port = 9000

buffer_size = 250000000    # 250mb

server.bind((host, port))
server.listen()

print("Listening at Server IP : {} & Port : {}".format(ip, str(port)))

client, address = server.accept()

print("{} is connected".format(address))

fd = open("received-file", "wb")
bytes_read = client.recv(buffer_size) # receiving file
fd.write(bytes_read)

client.close()
server.close()