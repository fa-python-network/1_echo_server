import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 7003))
print("Connection with server")
data = b''
while True:
    msg = input("Vvedite: ")
    if msg == "exit":
        sock.close()
        print('stop connection')
        break
    sock.send(msg.encode())
    print('send data to server')
    data += sock.recv(1024)
    print('new data from server')

if data:
    print(data.decode())
