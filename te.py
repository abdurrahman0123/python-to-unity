import socket


# The port number that Unity is listening on


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5005)
data = "dsbhasdkgb"
while True:
    
    sock.sendto(str.encode(str(data)), serverAddressPort)