import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))
while True:
    data = ""
    msg = input("Enter your message to server or 'exit' to quit: ")
    if msg.lower() == "exit":
        break
    sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
