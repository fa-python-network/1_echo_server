import socket

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

while True:
    message = input()
    sock.send(message.encode(ENCODING))
    recived = sock.recv(1024).decode(ENCODING)
    print(recived)
    if 'Closing connection' in recived:
        sock.close()
        break


