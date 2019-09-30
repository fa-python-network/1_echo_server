import os
import socket
import sys
from threading import Thread

sock = socket.socket()

address = input('Input address: ')
if not address:
    address = 'localhost'
port = input('Input port: ')
if not port:
    port = 9000
else:
    port = int(port)

sock.connect((address, port))
ENCODING = 'utf-8'
os.system('')


def receive_messages():
    while True:
        received = sock.recv(1024).decode(ENCODING)
        print(received)
        if 'Closing connection' in received:
            sock.close()
            break
    sys.exit()


Thread(target=receive_messages, daemon=True).start()

while True:
    message = input()
    sock.send(message.encode(ENCODING))
