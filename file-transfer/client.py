import socket

client = socket.socket()

ip = input("Enter IP of Server : ")
port = int(input("Enter Port of Server : "))

buffer_size = 250000000  # 250mb
filename = "send-file.mp3"   # file to send

client.connect((ip, port))

print("Connected to {} : {}".format(ip, port))

fd = open(filename, "rb")
bytes_read = fd.read(buffer_size)

client.sendall(bytes_read)  # sending file
print("Done....")

client.close()