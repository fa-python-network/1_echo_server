import socket

sock = socket.socket()

sock.connect(('localhost', 9095))

msg = "Hello, daria"
sock.send(msg.encode())

response = sock.recv(1024).decode()
print(response)