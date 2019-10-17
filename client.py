import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))

msg = input()
msg = "Hello!"
sock.send(msg.encode())

data = sock.recv(1024)
print('Put the hostname:')
hostname = input()
print('Put the port:')
port = input()

sock.close()
if int(port) > 1024 and int(port) < 65000:
    port_one = int(user_port)
else:
    port_one = 9099

print(data.decode())
sock.connect((hostname, port_one))
msg = "Hello!"
while True:
    mes = input()
    print('Your mesage: {mes}')
    sock.send(mes.encode())
    data = sock.recv(1024)
    print(data.decode())
    if mes == 'exit':
        print('exit')
        sock.close()
        break
