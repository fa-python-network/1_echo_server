import socket

sock = socket.socket()
sock.connect(('localhost',9093))
sock.send(b"Hello,dear!")
msg="hello"
sock.send(msg.encode())

response = sock.recv(1024).decode()
print(response)
