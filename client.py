import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
msg=input()
sock.send(msg)

data = sock.recv(1024)
sock.close()

print(data)