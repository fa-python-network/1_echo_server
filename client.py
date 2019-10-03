import socket


host = input("Input host address IPv4 or localhost, DEFAULT - 127.0.0.1: ")
host_list = host.split('.')
if host == 'localhost' and 0 < int(host_list[0]) <= 255 and 0 < int(host_list[1]) <= 255 and 0 < int(host_list[2]) <= 255 and 0 < int(host_list[3]) <= 255:
    pass
else:
    print("Data is not correct. Host is 127.0.0.1")
    host = '127.0.0.1'

port = input("Input port. Default - 9090: ")

try:
    port = int(port)
    if 1024 < port <= 65535:
        pass
    else:
        print("Data is not correct. Port is 9090")
        port = 9090
except:
    print("Data is not correct. Port is 9090")
    port = 9090

sock = socket.socket()
sock.connect((host, port))
msg = ''

while msg.lower().strip() != "exit":
    data = sock.recv(1024)
    print(data.decode())
    msg = input(' -> ')
    sock.send(msg.encode())