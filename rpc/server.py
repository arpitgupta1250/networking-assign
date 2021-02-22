from xmlrpc.server import SimpleXMLRPCServer   # library for rpc
import socket

def addition(n1,n2):
    return (n1 + n2)

def subtraction(n1,n2):
    return (n1 - n2)

def multiplication(n1,n2):
    return (n1 * n2)

def division(n1,n2):
    return (n1 / n2)

host = socket.gethostname()   # getting hostname
ip = socket.gethostbyname(host)   # getting ip
port = 9000

server = SimpleXMLRPCServer((ip, port))

print("Server IP : {}, Server Port : {}".format(ip,port))

# Registering function
server.register_function(addition, "addition")
server.register_function(subtraction, "subtraction")
server.register_function(multiplication, "multiplication")
server.register_function(division, "division")

server.serve_forever()