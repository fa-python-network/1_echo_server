import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9042))

while True:
    msg = input("Vvedite: ")
    if msg == "exit":
        data = sock.recv(1024)
        sock.close()
        break
    sock.send(msg.encode())




print(data.decode())
