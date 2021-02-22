from xmlrpc.client import ServerProxy

ip = input("Enter IP of server : ")
port = input("Enter port of server : ")

proxy = ServerProxy("http://{}:{}/".format(ip,port))

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

# rpc
add = proxy.addition(n1,n2)
sub = proxy.subtraction(n1,n2)
mul = proxy.multiplication(n1,n2)
div = proxy.division(n1,n2)

print("Addition of {} and {} : {}".format(n1,n2,add))
print("Subtraction of {} and {} : {}".format(n1,n2,sub))
print("Multiplication of {} and {} : {}".format(n1,n2,mul))
print("Division of {} and {} : {}".format(n1,n2,div))