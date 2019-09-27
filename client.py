import socket
from time import sleep
import logging as log

log.basicConfig(format='%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=log.DEBUG)

ADDRESS, PORT = 'localhost', 9797

address_ = input(f'Address (empty for {ADDRESS}): ')
ADDRESS = address_ if address_ else ADDRESS
port_ = input(f'Port (empty for {PORT}): ')
PORT = port_ if port_ else PORT


sock = socket.socket()
log.debug('Socket sterted')
sock.connect((ADDRESS, PORT))
log.info(f'Connected to {ADDRESS}:{PORT}')

msg = input('<= ')

log.debug(f'Sending "{msg}"')
sock.send(msg.encode())

log.debug('Receiving data from server')
data = sock.recv(1024)

log.debug(f'Disconnecting from {ADDRESS}:{PORT}')
sock.close()

print(f'=> {data.decode()}')
# sock.close()
