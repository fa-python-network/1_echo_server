import socket
from time import sleep
import logging as log

log.basicConfig(filename='client.log', format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)

ADDRESS, PORT = 'localhost', 9797

address_ = input(f'Address (empty for {ADDRESS}): ')
ADDRESS = address_ if address_ else ADDRESS
port_ = input(f'Port (empty for {PORT}): ')
PORT = int(port_) if port_ else PORT


sock = socket.socket()
log.debug('Socket started')
sock.connect((ADDRESS, PORT))
log.info(f'Connected to {ADDRESS}:{PORT}')

data = sock.recv(1024)
if 'Enter your name' in data.decode():
    name = input(data.decode())
    sock.send(name.encode())
else:
    print(data.decode())

while True:

    msg = input('<= ')

    if msg == '/disconnect':
        break

    log.debug(f'Sending "{msg}"')
    sock.send(msg.encode())

    log.debug('Receiving data from server')
    data = sock.recv(1024)

    log.debug(f'Disconnecting from {ADDRESS}:{PORT}')

    print(f'=> {data.decode()}')

sock.close()
