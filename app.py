import os
import socket
import sys
from threading import Thread
from common import SocketMethods

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
os.system('')

try:
    with open('token', 'r') as file:
        token = file.read()
except FileNotFoundError:
    token = '--no token--'
SocketMethods.send_text(sock, token)

connection_alive = True


def receive_messages():
    global connection_alive
    while True:
        received = SocketMethods.receive_text(sock)
        if received[:2] == '//':
            if received == '//close':
                sock.close()
                connection_alive = False
                break
            if received == '//token':
                with open('token', 'w') as file:
                    file.write(SocketMethods.receive_text(sock))
                continue
        print(received)
    sys.exit()


Thread(target=receive_messages, daemon=True).start()

while True:
    message = input()
    if connection_alive:
        SocketMethods.send_text(sock, message)
    else:
        break
