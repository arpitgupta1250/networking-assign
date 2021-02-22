import socket
import threading

name = input("Enter your name : ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Enter IP of Server : ")
port = int(input("Enter Port of Server : "))

client.connect((ip, port))

# Listening to server and sending name
def receive():
  while True:
    try:
      # Receive message from server
      message = client.recv(1024).decode()
      if message == 'name':
        client.send(name.encode())
      else:
        print(message)
    except:
      # Close connection when error
      print("An error occured!")
      client.close()
      break

# Sending messages to server
def write():
    while True:
        message = '{}: {}'.format(name, input(""))
        client.send(message.encode())


# Threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()