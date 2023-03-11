import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5005)
data = "dsbhasdkgb"

while True: # for continues
    
    sock.sendto(str.encode(str(data)), serverAddressPort)
