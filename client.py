import socket
from threading import Thread


while True:
    try:
        data = sock.recv(1024)
        msg = data.decode()
        print(msg)
    except:
        break

try:
    sock = socket.socket()
    print('Jot down host')
    host = input()
    print('Jot down  port')
    port = int(input())
    sock.connect((host, port))
except:
    host = 'localhost'
    port = 9095
    sock.connect((host, port))

print('Jot down passwd"')
passwd = input()
msg = passwd
sock.send(msg.encode())

Thread(target=check).start()

while msg !="close":
    msg = input()
    if msg !='close':
        sock.send(msg.encode())




msg = 'disconnected'
sock.send(msg.encode())
data = sock.recv(1024)

sock.close()
