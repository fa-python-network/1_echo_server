import socket
from time import sleep

sock = socket.socket()
sock.setblocking(True)
sock.connect(('localhost', 9090))
msg = input()
while msg != 'exit':
    sock.send(msg.encode())
    msg = input()

sock.close()
